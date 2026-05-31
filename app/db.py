import pyodbc

from app.config import (
    SQL_SERVER,
    SQL_DATABASE,
    SQL_USERNAME,
    SQL_PASSWORD,
    SQL_AUTH_MODE,
)


def build_connection_string():
    print("[1] Starting to build SQL Server connection string...")

    driver = "ODBC Driver 18 for SQL Server"
    print(f"[2] Using ODBC driver: {driver}")

    auth_mode = SQL_AUTH_MODE.lower().strip()
    print(f"[3] Authentication mode from .env: {auth_mode}")

    print(f"[4] SQL Server: {SQL_SERVER}")
    print(f"[5] SQL Database: {SQL_DATABASE}")

    if auth_mode == "sql":
        print("[6] Building connection string for SQL Server Authentication...")
        print(f"[7] SQL Username: {SQL_USERNAME}")
        print("[8] SQL Password: ******")

        connection_string = (
            f"DRIVER={{{driver}}};"
            f"SERVER={SQL_SERVER};"
            f"DATABASE={SQL_DATABASE};"
            f"UID={SQL_USERNAME};"
            f"PWD={SQL_PASSWORD};"
            "Encrypt=yes;"
            "TrustServerCertificate=yes;"
        )

        print("[9] Connection string was built successfully.")
        return connection_string

    print("[6] Building connection string for Windows Authentication...")

    connection_string = (
        f"DRIVER={{{driver}}};"
        f"SERVER={SQL_SERVER};"
        f"DATABASE={SQL_DATABASE};"
        "Trusted_Connection=yes;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
        
    )

    print("[7] Connection string was built successfully.")
    return connection_string


def get_connection():
    print("[10] Opening connection to SQL Server...")

    connection_string = build_connection_string()

    print("[11] Calling pyodbc.connect()...")
    conn = pyodbc.connect(connection_string)

    print("[12] SQL Server connection opened successfully.")
    return conn


def test_connection():
    print("[13] Starting SQL Server connection test...")

    conn = get_connection()
    print("[14] Connection object received.")

    cursor = conn.cursor()
    print("[15] Cursor created successfully.")

    print("[16] Executing test query...")
    cursor.execute("""
        SELECT
            @@SERVERNAME AS ServerName,
            DB_NAME() AS DatabaseName,
            SUSER_SNAME() AS LoginName,
            SYSTEM_USER AS SystemUser
    """)

    print("[17] Query executed successfully.")

    row = cursor.fetchone()
    print("[18] Result row fetched successfully.")

    cursor.close()
    print("[19] Cursor closed.")

    conn.close()
    print("[20] Connection closed.")

    result = {
        "server_name": row.ServerName,
        "database_name": row.DatabaseName,
        "login_name": row.LoginName,
        "system_user": row.SystemUser,
    }

    print("[21] Test result dictionary created.")
    return result


def get_table_counts():
    print("[COUNTS-1] Starting table counts query...")

    conn = get_connection()
    print("[COUNTS-2] SQL Server connection opened.")

    cursor = conn.cursor()
    print("[COUNTS-3] Cursor created.")

    query = """
        SELECT 'Customers' AS TableName, COUNT(*) AS RowCountValue FROM dbo.Customers
        UNION ALL
        SELECT 'Products' AS TableName, COUNT(*) AS RowCountValue FROM dbo.Products
        UNION ALL
        SELECT 'Orders' AS TableName, COUNT(*) AS RowCountValue FROM dbo.Orders
        UNION ALL
        SELECT 'OrderItems' AS TableName, COUNT(*) AS RowCountValue FROM dbo.OrderItems
        UNION ALL
        SELECT 'DBA_KnowledgeBase' AS TableName, COUNT(*) AS RowCountValue FROM dbo.DBA_KnowledgeBase
        UNION ALL
        SELECT 'AI_QuestionHistory' AS TableName, COUNT(*) AS RowCountValue FROM dbo.AI_QuestionHistory
    """

    print("[COUNTS-4] Executing table counts query...")
    cursor.execute(query)
    print("[COUNTS-5] Query executed successfully.")

    rows = cursor.fetchall()
    print("[COUNTS-6] Rows fetched successfully.")

    result = []

    for row in rows:
        result.append({
            "table_name": row.TableName,
            "row_count": row.RowCountValue,
        })

    print("[COUNTS-7] Result list created.")

    cursor.close()
    print("[COUNTS-8] Cursor closed.")

    conn.close()
    print("[COUNTS-9] Connection closed.")

    return result