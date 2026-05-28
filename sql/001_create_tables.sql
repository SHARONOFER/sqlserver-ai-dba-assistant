USE DBA_AI_Assistant;
GO

PRINT 'Starting table creation script...';
GO

IF OBJECT_ID('dbo.Customers', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Customers
    (
        CustomerID INT IDENTITY(1,1) PRIMARY KEY,
        CustomerName NVARCHAR(100) NOT NULL,
        Email NVARCHAR(200) NULL,
        CreatedAt DATETIME2 NOT NULL DEFAULT SYSDATETIME()
    );

    PRINT 'Table dbo.Customers created successfully.';
END
ELSE
BEGIN
    PRINT 'Table dbo.Customers already exists.';
END
GO

IF OBJECT_ID('dbo.Products', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Products
    (
        ProductID INT IDENTITY(1,1) PRIMARY KEY,
        ProductName NVARCHAR(100) NOT NULL,
        Category NVARCHAR(50) NOT NULL,
        Price DECIMAL(10,2) NOT NULL
    );

    PRINT 'Table dbo.Products created successfully.';
END
ELSE
BEGIN
    PRINT 'Table dbo.Products already exists.';
END
GO

IF OBJECT_ID('dbo.Orders', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Orders
    (
        OrderID INT IDENTITY(1,1) PRIMARY KEY,
        CustomerID INT NOT NULL,
        OrderDate DATETIME2 NOT NULL DEFAULT SYSDATETIME(),
        TotalAmount DECIMAL(10,2) NOT NULL,

        CONSTRAINT FK_Orders_Customers
            FOREIGN KEY (CustomerID)
            REFERENCES dbo.Customers(CustomerID)
    );

    PRINT 'Table dbo.Orders created successfully.';
END
ELSE
BEGIN
    PRINT 'Table dbo.Orders already exists.';
END
GO

IF OBJECT_ID('dbo.OrderItems', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.OrderItems
    (
        OrderItemID INT IDENTITY(1,1) PRIMARY KEY,
        OrderID INT NOT NULL,
        ProductID INT NOT NULL,
        Quantity INT NOT NULL,
        UnitPrice DECIMAL(10,2) NOT NULL,

        CONSTRAINT FK_OrderItems_Orders
            FOREIGN KEY (OrderID)
            REFERENCES dbo.Orders(OrderID),

        CONSTRAINT FK_OrderItems_Products
            FOREIGN KEY (ProductID)
            REFERENCES dbo.Products(ProductID)
    );

    PRINT 'Table dbo.OrderItems created successfully.';
END
ELSE
BEGIN
    PRINT 'Table dbo.OrderItems already exists.';
END
GO

IF OBJECT_ID('dbo.DBA_KnowledgeBase', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.DBA_KnowledgeBase
    (
        KnowledgeID INT IDENTITY(1,1) PRIMARY KEY,
        Title NVARCHAR(200) NOT NULL,
        Category NVARCHAR(100) NOT NULL,
        Content NVARCHAR(MAX) NOT NULL,
        CreatedAt DATETIME2 NOT NULL DEFAULT SYSDATETIME()
    );

    PRINT 'Table dbo.DBA_KnowledgeBase created successfully.';
END
ELSE
BEGIN
    PRINT 'Table dbo.DBA_KnowledgeBase already exists.';
END
GO

IF OBJECT_ID('dbo.AI_QuestionHistory', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.AI_QuestionHistory
    (
        QuestionID INT IDENTITY(1,1) PRIMARY KEY,
        UserQuestion NVARCHAR(MAX) NOT NULL,
        AIAnswer NVARCHAR(MAX) NULL,
        CreatedAt DATETIME2 NOT NULL DEFAULT SYSDATETIME()
    );

    PRINT 'Table dbo.AI_QuestionHistory created successfully.';
END
ELSE
BEGIN
    PRINT 'Table dbo.AI_QuestionHistory already exists.';
END
GO

PRINT 'Table creation script finished.';
GO