USE DBA_AI_Assistant;
GO

IF NOT EXISTS (
    SELECT 1
    FROM sys.tables
    WHERE name = 'AI_DiagnosticRunHistory'
      AND schema_id = SCHEMA_ID('dbo')
)
BEGIN
    CREATE TABLE dbo.AI_DiagnosticRunHistory
    (
        RunID INT IDENTITY(1,1) NOT NULL PRIMARY KEY,

        UserQuestion NVARCHAR(MAX) NOT NULL,

        SelectedTools NVARCHAR(MAX) NULL,

        KnowledgeArticlesUsed NVARCHAR(MAX) NULL,

        DiagnosticContext NVARCHAR(MAX) NULL,

        AIAnswer NVARCHAR(MAX) NULL,

        CreatedAt DATETIME2(3) NOT NULL
            CONSTRAINT DF_AI_DiagnosticRunHistory_CreatedAt
            DEFAULT SYSUTCDATETIME()
    );
END;
GO