USE DBA_AI_Assistant;
GO

PRINT 'Starting sample data insert script...';
GO

IF NOT EXISTS (SELECT 1 FROM dbo.Customers)
BEGIN
    INSERT INTO dbo.Customers (CustomerName, Email)
    VALUES
    (N'Israel Tech Ltd', N'contact@israeltech.co.il'),
    (N'Data World', N'info@dataworld.com'),
    (N'Sharon Consulting', N'sharon@example.com');

    PRINT 'Sample customers inserted successfully.';
END
ELSE
BEGIN
    PRINT 'Customers table already contains data. Skipping insert.';
END
GO

IF NOT EXISTS (SELECT 1 FROM dbo.Products)
BEGIN
    INSERT INTO dbo.Products (ProductName, Category, Price)
    VALUES
    (N'SQL Server Monitoring Package', N'DBA Tools', 1200.00),
    (N'Performance Tuning Session', N'Consulting', 2500.00),
    (N'Backup Strategy Review', N'DBA Services', 1800.00);

    PRINT 'Sample products inserted successfully.';
END
ELSE
BEGIN
    PRINT 'Products table already contains data. Skipping insert.';
END
GO

IF NOT EXISTS (SELECT 1 FROM dbo.Orders)
BEGIN
    INSERT INTO dbo.Orders (CustomerID, TotalAmount)
    VALUES
    (1, 3700.00),
    (2, 1800.00),
    (3, 1200.00);

    PRINT 'Sample orders inserted successfully.';
END
ELSE
BEGIN
    PRINT 'Orders table already contains data. Skipping insert.';
END
GO

IF NOT EXISTS (SELECT 1 FROM dbo.OrderItems)
BEGIN
    INSERT INTO dbo.OrderItems (OrderID, ProductID, Quantity, UnitPrice)
    VALUES
    (1, 1, 1, 1200.00),
    (1, 2, 1, 2500.00),
    (2, 3, 1, 1800.00),
    (3, 1, 1, 1200.00);

    PRINT 'Sample order items inserted successfully.';
END
ELSE
BEGIN
    PRINT 'OrderItems table already contains data. Skipping insert.';
END
GO

IF NOT EXISTS (SELECT 1 FROM dbo.DBA_KnowledgeBase)
BEGIN
    INSERT INTO dbo.DBA_KnowledgeBase (Title, Category, Content)
    VALUES
    (
        N'High CPU Troubleshooting',
        N'Performance',
        N'When SQL Server has high CPU usage, check top queries by CPU, execution count, Query Store, wait stats, missing indexes, and recent deployments.'
    ),
    (
        N'Blocking Troubleshooting',
        N'Performance',
        N'When users report slowness, check blocking sessions, open transactions, locks, wait types, and long-running queries.'
    ),
    (
        N'Backup Failure Troubleshooting',
        N'Backup',
        N'When a backup fails, check SQL Server error log, job history, disk space, permissions, backup path, and recent changes.'
    );

    PRINT 'Sample DBA knowledge base records inserted successfully.';
END
ELSE
BEGIN
    PRINT 'DBA_KnowledgeBase table already contains data. Skipping insert.';
END
GO

PRINT 'Sample data insert script finished.';
GO