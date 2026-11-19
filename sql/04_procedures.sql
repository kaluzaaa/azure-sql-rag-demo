-- Hybrid search over speaker turns: three legs ranked separately, fused with
-- Reciprocal Rank Fusion: score = SUM over legs of weight / (60 + rank in the leg).
--   fulltext: Polish FREETEXT, finds inflected forms ("kontenerów" -> "kontener")
--   phrase:   the words of the text as one exact phrase (skipped for fewer than two words)
--   vector:   cosine distance to @embedding, exact scan (works with or without a vector index)
-- Each leg keeps its top 50 inside the date range. A NULL date is an open bound.
CREATE OR ALTER PROCEDURE dbo.SearchChunks
    @searchText NVARCHAR(4000),
    @embedding  VECTOR(1536),
    @topK       INT = 10,
    @fromDate   DATE = NULL,
    @toDate     DATE = NULL,
    @wVector    FLOAT = 2
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @candidates INT = 50;
    DECLARE @phrase NVARCHAR(4000) = dbo.FulltextPhraseCondition(@searchText);
    DECLARE @hasWords BIT = IIF(EXISTS (SELECT 1 FROM dbo.FulltextWords(@searchText)), 1, 0);
    SET @fromDate = ISNULL(@fromDate, '0001-01-01');
    SET @toDate = ISNULL(@toDate, '9999-12-31');

    CREATE TABLE #Legs (leg VARCHAR(10), chunk_id INT, leg_rank INT, weight FLOAT);

    IF @hasWords = 1  -- FREETEXT raises an error on empty or whitespace-only text
        INSERT INTO #Legs
        SELECT TOP (@candidates) 'fulltext', c.chunk_id,
               ROW_NUMBER() OVER (ORDER BY ft.RANK DESC, c.chunk_id), 1
        FROM FREETEXTTABLE(dbo.TranscriptChunks, transcript_text, @searchText, LANGUAGE 1045) AS ft
        JOIN dbo.TranscriptChunks AS c ON c.chunk_id = ft.[KEY]
        WHERE c.publication_date BETWEEN @fromDate AND @toDate
        ORDER BY ft.RANK DESC, c.chunk_id;

    IF @phrase IS NOT NULL
        INSERT INTO #Legs
        SELECT TOP (@candidates) 'phrase', c.chunk_id,
               ROW_NUMBER() OVER (ORDER BY ct.RANK DESC, c.chunk_id), 1
        FROM CONTAINSTABLE(dbo.TranscriptChunks, transcript_text, @phrase, LANGUAGE 1045) AS ct
        JOIN dbo.TranscriptChunks AS c ON c.chunk_id = ct.[KEY]
        WHERE c.publication_date BETWEEN @fromDate AND @toDate
        ORDER BY ct.RANK DESC, c.chunk_id;

    IF @embedding IS NOT NULL
        INSERT INTO #Legs
        SELECT TOP (@candidates) 'vector', c.chunk_id,
               ROW_NUMBER() OVER (ORDER BY d.distance, c.chunk_id), @wVector
        FROM dbo.TranscriptChunks AS c
        CROSS APPLY (SELECT VECTOR_DISTANCE('cosine', c.embedding, @embedding) AS distance) AS d
        WHERE c.publication_date BETWEEN @fromDate AND @toDate
        ORDER BY d.distance, c.chunk_id;

    WITH fused AS (
        SELECT chunk_id,
               SUM(weight / (60 + leg_rank)) AS score,
               MIN(IIF(leg = 'fulltext', leg_rank, NULL)) AS rank_fulltext,
               MIN(IIF(leg = 'phrase', leg_rank, NULL)) AS rank_phrase,
               MIN(IIF(leg = 'vector', leg_rank, NULL)) AS rank_vector
        FROM #Legs
        GROUP BY chunk_id
    )
    SELECT TOP (@topK)
        c.episode_number, e.title, c.publication_date, c.chunk_number, c.speaker,
        c.start_timestamp, c.transcript_text, f.score,
        f.rank_fulltext, f.rank_phrase, f.rank_vector
    FROM fused AS f
    JOIN dbo.TranscriptChunks AS c ON c.chunk_id = f.chunk_id
    JOIN dbo.Episodes AS e ON e.episode_number = c.episode_number
    ORDER BY f.score DESC, c.episode_number DESC, c.chunk_number;
END;
GO

-- How many turns per episode hold every word of the text (each word as a prefix).
-- An aggregate, not a top-k list: no ranking, no vector leg.
CREATE OR ALTER PROCEDURE dbo.CountMentions
    @searchText NVARCHAR(4000),
    @fromDate   DATE = NULL,
    @toDate     DATE = NULL
AS
BEGIN
    SET NOCOUNT ON;
    DECLARE @condition NVARCHAR(4000) = dbo.FulltextAllWordsCondition(@searchText);
    SET @fromDate = ISNULL(@fromDate, '0001-01-01');
    SET @toDate = ISNULL(@toDate, '9999-12-31');

    DECLARE @counts TABLE (episode_number INT PRIMARY KEY, mention_count INT NOT NULL);

    -- CONTAINS raises an error on a NULL condition, even behind a WHERE guard,
    -- so text without a searchable word skips it and returns no rows.
    IF @condition IS NOT NULL
        INSERT INTO @counts (episode_number, mention_count)
        SELECT episode_number, COUNT(*)
        FROM dbo.TranscriptChunks
        WHERE CONTAINS(transcript_text, @condition, LANGUAGE 1045)
          AND publication_date BETWEEN @fromDate AND @toDate
        GROUP BY episode_number;

    SELECT c.episode_number, e.title, e.publication_date, c.mention_count
    FROM @counts AS c
    JOIN dbo.Episodes AS e ON e.episode_number = c.episode_number
    ORDER BY c.mention_count DESC, c.episode_number DESC;
END;
