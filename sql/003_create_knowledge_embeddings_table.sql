USE DBA_AI_Assistant;
GO

PRINT 'Starting knowledge base embeddings table creation script...';
GO

IF OBJECT_ID('dbo.DBA_KnowledgeBaseEmbeddings', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.DBA_KnowledgeBaseEmbeddings
    (
        EmbeddingID INT IDENTITY(1,1) NOT NULL,
        KnowledgeID INT NOT NULL,
        EmbeddingModel NVARCHAR(100) NOT NULL,
        Embedding VECTOR(1536) NOT NULL,
        CreatedAt DATETIME2 NOT NULL 
            CONSTRAINT DF_DBA_KnowledgeBaseEmbeddings_CreatedAt 
            DEFAULT SYSDATETIME(),

        CONSTRAINT PK_DBA_KnowledgeBaseEmbeddings
            PRIMARY KEY (EmbeddingID),

        CONSTRAINT FK_DBA_KnowledgeBaseEmbeddings_DBA_KnowledgeBase
            FOREIGN KEY (KnowledgeID)
            REFERENCES dbo.DBA_KnowledgeBase(KnowledgeID),

        CONSTRAINT UQ_DBA_KnowledgeBaseEmbeddings_KnowledgeID_Model
            UNIQUE (KnowledgeID, EmbeddingModel)
    );

    PRINT 'Table dbo.DBA_KnowledgeBaseEmbeddings created successfully.';
END
ELSE
BEGIN
    PRINT 'Table dbo.DBA_KnowledgeBaseEmbeddings already exists.';
END
GO

PRINT 'Knowledge base embeddings table creation script finished.';
GO