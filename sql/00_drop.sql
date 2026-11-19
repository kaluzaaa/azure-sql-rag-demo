-- Drop every demo object, so the next files build the schema from scratch.
-- Dropping a table also drops its full-text index and its vector index.
DROP PROCEDURE IF EXISTS dbo.SearchChunks, dbo.CountMentions;
DROP FUNCTION IF EXISTS dbo.FulltextPhraseCondition, dbo.FulltextAllWordsCondition, dbo.FulltextWords;
DROP TABLE IF EXISTS
    dbo.EpisodeTags, dbo.EpisodeChapters, dbo.EpisodeGuests, dbo.People,
    dbo.EpisodeLinks, dbo.Links, dbo.TranscriptChunks, dbo.Episodes;
GO
IF EXISTS (SELECT 1 FROM sys.fulltext_catalogs WHERE name = 'DemoCatalog')
    DROP FULLTEXT CATALOG DemoCatalog;
