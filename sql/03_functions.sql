-- Safe full-text conditions built from free text.
-- Only word tokens (runs of letters and digits) reach CONTAINS, so quotes, operators
-- and other punctuation in the user's text can never break the condition.

-- The words of a text with the position of their first character.
-- A letter is a character whose upper and lower case differ.
CREATE OR ALTER FUNCTION dbo.FulltextWords (@text NVARCHAR(4000))
RETURNS TABLE
AS
RETURN
    WITH chars AS (
        SELECT s.value AS pos, SUBSTRING(@text, s.value, 1) AS c
        FROM GENERATE_SERIES(1, LEN(@text)) AS s
    ),
    letters AS (
        -- consecutive letters share the same word_id
        SELECT pos, c, pos - ROW_NUMBER() OVER (ORDER BY pos) AS word_id
        FROM chars
        WHERE UNICODE(UPPER(c)) <> UNICODE(LOWER(c)) OR c LIKE N'[0-9]'
    )
    SELECT MIN(pos) AS pos, STRING_AGG(c, N'') WITHIN GROUP (ORDER BY pos) AS word
    FROM letters
    GROUP BY word_id;
GO

-- Exact phrase: 'vendor lock-in' -> '"vendor lock in"'. NULL for fewer than two words.
CREATE OR ALTER FUNCTION dbo.FulltextPhraseCondition (@text NVARCHAR(4000))
RETURNS NVARCHAR(4000)
AS
BEGIN
    DECLARE @words INT, @phrase NVARCHAR(4000);

    SELECT @words = COUNT(*),
           @phrase = N'"' + STRING_AGG(word, N' ') WITHIN GROUP (ORDER BY pos) + N'"'
    FROM dbo.FulltextWords(LEFT(@text, 1000));

    RETURN IIF(@words >= 2, @phrase, NULL);
END;
GO

-- Every word as a prefix: 'Kubernetes w chmurze' -> '"chmurze*" AND "Kubernetes*"'.
-- Polish stopwords are skipped: the index does not store them. NULL when no word is left.
CREATE OR ALTER FUNCTION dbo.FulltextAllWordsCondition (@text NVARCHAR(4000))
RETURNS NVARCHAR(4000)
AS
BEGIN
    DECLARE @condition NVARCHAR(4000);

    SELECT @condition = STRING_AGG(N'"' + word + N'*"', N' AND ') WITHIN GROUP (ORDER BY word)
    FROM (SELECT DISTINCT word FROM dbo.FulltextWords(LEFT(@text, 400))) AS w
    WHERE NOT EXISTS (
        SELECT 1 FROM sys.fulltext_system_stopwords AS s
        WHERE s.language_id = 1045 AND s.stopword = w.word
    );

    RETURN @condition;
END;
