USE DBA_AI_Assistant;
GO

CREATE OR ALTER PROCEDURE dbo.usp_DemoCpu_HashWork
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @i INT = 0;
    DECLARE @hash VARBINARY(32) = 0x01;

    WHILE @i < 50000
    BEGIN
        SET @hash = HASHBYTES('SHA2_256', @hash);
        SET @i += 1;
    END;

    SELECT @hash AS final_hash;
END;
GO


CREATE OR ALTER PROCEDURE dbo.usp_DemoCpu_MathWork
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @i INT = 1;
    DECLARE @result FLOAT = 0;

    WHILE @i < 200000
    BEGIN
        SET @result = @result + SQRT(@i) * SIN(@i);
        SET @i += 1;
    END;

    SELECT @result AS final_result;
END;
GO


CREATE OR ALTER PROCEDURE dbo.usp_DemoCpu_StringWork
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @i INT = 0;
    DECLARE @txt NVARCHAR(200) = N'SQL Server DBA Assistant CPU Demo';

    WHILE @i < 50000
    BEGIN
        SET @txt = REVERSE(@txt);
        SET @txt = LOWER(UPPER(@txt));
        SET @i += 1;
    END;

    SELECT LEFT(@txt, 100) AS final_text;
END;
GO