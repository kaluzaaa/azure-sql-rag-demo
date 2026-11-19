-- Tables. Embeddings: text-embedding-3-small, 1536 dimensions, computed in Python.

CREATE TABLE dbo.Episodes (
    episode_number   INT            NOT NULL CONSTRAINT PK_Episodes PRIMARY KEY,
    title            NVARCHAR(400)  NOT NULL,
    publication_date DATE           NOT NULL,
    summary          NVARCHAR(MAX)  NOT NULL,
    tags             NVARCHAR(1000) NOT NULL,  -- comma-separated, for full-text search
    youtube_id       VARCHAR(20)    NULL,
    title_embedding  VECTOR(1536)   NOT NULL   -- input: "Title: <title>\nTags: <tags>"
);

-- One row per speaker turn.
CREATE TABLE dbo.TranscriptChunks (
    chunk_id         INT IDENTITY   NOT NULL CONSTRAINT PK_TranscriptChunks PRIMARY KEY,
    episode_number   INT            NOT NULL REFERENCES dbo.Episodes (episode_number),
    chunk_number     INT            NOT NULL,
    publication_date DATE           NOT NULL,  -- copy of Episodes.publication_date for filters
    speaker          NVARCHAR(100)  NOT NULL,
    start_timestamp  VARCHAR(12)    NOT NULL,  -- HH:MM:SS.xx
    transcript_text  NVARCHAR(MAX)  NOT NULL,
    embedding        VECTOR(1536)   NOT NULL,
    CONSTRAINT UQ_TranscriptChunks UNIQUE (episode_number, chunk_number)
);

CREATE TABLE dbo.Links (
    link_slug VARCHAR(200)   NOT NULL CONSTRAINT PK_Links PRIMARY KEY,
    url       NVARCHAR(2000) NOT NULL,
    title     NVARCHAR(400)  NOT NULL,
    author    NVARCHAR(200)  NULL,
    created   DATE           NULL,
    tldr      NVARCHAR(MAX)  NULL,      -- one sentence per line
    tags      NVARCHAR(1000) NULL,      -- comma-separated
    embedding VECTOR(1536)   NOT NULL
);

CREATE TABLE dbo.EpisodeLinks (
    episode_number INT          NOT NULL REFERENCES dbo.Episodes (episode_number),
    link_slug      VARCHAR(200) NOT NULL REFERENCES dbo.Links (link_slug),
    position       INT          NOT NULL,
    CONSTRAINT PK_EpisodeLinks PRIMARY KEY (episode_number, link_slug)
);

CREATE TABLE dbo.People (
    person_slug VARCHAR(100)  NOT NULL CONSTRAINT PK_People PRIMARY KEY,
    name        NVARCHAR(200) NOT NULL
);

CREATE TABLE dbo.EpisodeGuests (
    episode_number INT          NOT NULL REFERENCES dbo.Episodes (episode_number),
    person_slug    VARCHAR(100) NOT NULL REFERENCES dbo.People (person_slug),
    CONSTRAINT PK_EpisodeGuests PRIMARY KEY (episode_number, person_slug)
);

CREATE TABLE dbo.EpisodeChapters (
    episode_number  INT           NOT NULL REFERENCES dbo.Episodes (episode_number),
    position        INT           NOT NULL,
    start_timestamp VARCHAR(8)    NOT NULL,  -- HH:MM:SS
    title           NVARCHAR(400) NOT NULL,
    CONSTRAINT PK_EpisodeChapters PRIMARY KEY (episode_number, position)
);

CREATE TABLE dbo.EpisodeTags (
    episode_number INT           NOT NULL REFERENCES dbo.Episodes (episode_number),
    tag            NVARCHAR(100) NOT NULL,
    CONSTRAINT PK_EpisodeTags PRIMARY KEY (episode_number, tag)
);
