import pyodbc
import json

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
        print("[6] Building connection string for SQL   " \
        "" \
        "" \
        "  Server Authentication...")
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


def get_knowledge_base_articles():
    print("[KB-1] Starting knowledge base query...")

    conn = get_connection()
    print("[KB-2] SQL Server connection opened.")

    cursor = conn.cursor()
    print("[KB-3] Cursor created.")

    query = """
        SELECT
            KnowledgeID,
            Title,
            Category,
            Content,
            CreatedAt
        FROM dbo.DBA_KnowledgeBase
        ORDER BY KnowledgeID;    """


    print("[KB-4] Executing knowledge base query...")
    cursor.execute(query)
    print("[KB-5] Query executed successfully.")

    rows = cursor.fetchall()
    print("[KB-6] Rows fetched successfully.")

    result = []

    for row in rows:
        result.append({
            "knowledge_id": row.KnowledgeID,
            "title": row.Title,
            "category": row.Category,
            "content": row.Content,
            "created_at": row.CreatedAt,
        })

    print("[KB-7] Result list created.")

    cursor.close()
    print("[KB-8] Cursor closed.")

    conn.close()
    print("[KB-9] Connection closed.")

    return result


def vector_to_sql_json(vector):

    """
    Converts a Python embedding vector list into a JSON string.
    SQL Server receives this JSON text and casts it into VECTOR(1536)
    for vector distance comparison.
    """
    
    print("[VECTOR-1] Converting Python vector to SQL Server vector JSON text...")

    vector_json = json.dumps(vector)

    print("[VECTOR-2] Vector was converted to JSON text successfully.")
    return vector_json



def save_knowledge_embedding(knowledge_id, embedding_model, embedding_vector):
    print("[SAVE-EMBED-1] Starting knowledge embedding save process...")

    embedding_json = vector_to_sql_json(embedding_vector)
    print("[SAVE-EMBED-2] Embedding vector converted to SQL JSON text.")

    conn = get_connection()
    print("[SAVE-EMBED-3] SQL Server connection opened.")

    cursor = conn.cursor()
    print("[SAVE-EMBED-4] Cursor created.")

    query = """
        IF EXISTS (
            SELECT 1
            FROM dbo.DBA_KnowledgeBaseEmbeddings
            WHERE KnowledgeID = ?
              AND EmbeddingModel = ?
        )
        BEGIN
            UPDATE dbo.DBA_KnowledgeBaseEmbeddings
            SET Embedding = CAST(CAST(? AS NVARCHAR(MAX)) AS VECTOR(1536)),
                CreatedAt = SYSDATETIME()
            WHERE KnowledgeID = ?
              AND EmbeddingModel = ?;
        END
        ELSE
        BEGIN
            INSERT INTO dbo.DBA_KnowledgeBaseEmbeddings
            (
                KnowledgeID,
                EmbeddingModel,
                Embedding
            )
            VALUES
            (
                ?,
                ?,
               CAST(CAST(? AS NVARCHAR(MAX)) AS VECTOR(1536))
            );
        END
    """

    print("[SAVE-EMBED-5] Executing insert/update embedding query...")

    cursor.execute(
        query,
        knowledge_id,
        embedding_model,
        embedding_json,
        knowledge_id,
        embedding_model,
        knowledge_id,
        embedding_model,
        embedding_json,
    )

    print("[SAVE-EMBED-6] Query executed successfully.")

    conn.commit()
    print("[SAVE-EMBED-7] Transaction committed.")

    cursor.close()
    print("[SAVE-EMBED-8] Cursor closed.")

    conn.close()
    print("[SAVE-EMBED-9] Connection closed.")

    print("[SAVE-EMBED-10] Knowledge embedding saved successfully.")

def get_relevant_knowledge_articles_by_vector(question_vector_json, top_n=3):

    """
    Searches SQL Server for the most relevant knowledge base articles
    by comparing the user's question vector against stored article vectors
    using VECTOR_DISTANCE.
    """
    print("[VECTOR-SEARCH-1] Starting relevant knowledge vector search...")

    conn = get_connection()
    print("[VECTOR-SEARCH-2] SQL Server connection opened.")

    cursor = conn.cursor()
    print("[VECTOR-SEARCH-3] Cursor created.")

    query = """
        SELECT TOP (?)
            kb.KnowledgeID,
            kb.Title,
            kb.Category,
            kb.Content,
            VECTOR_DISTANCE(
                'cosine',
                CAST(CAST(? AS NVARCHAR(MAX)) AS VECTOR(1536)),
                e.Embedding
            ) AS DistanceValue
        FROM dbo.DBA_KnowledgeBaseEmbeddings e
        JOIN dbo.DBA_KnowledgeBase kb
            ON e.KnowledgeID = kb.KnowledgeID
        WHERE e.EmbeddingModel = 'local-hash-v1'
        ORDER BY DistanceValue ASC;
    """

    print("[VECTOR-SEARCH-4] Executing vector search query...")

    cursor.execute(query, top_n, question_vector_json)

    print("[VECTOR-SEARCH-5] Query executed successfully.")

    rows = cursor.fetchall()
    print("[VECTOR-SEARCH-6] Rows fetched successfully.")

    result = []

    for row in rows:
        result.append({
            "knowledge_id": row.KnowledgeID,
            "title": row.Title,
            "category": row.Category,
            "content": row.Content,
            "distance": row.DistanceValue,
        })

    print("[VECTOR-SEARCH-7] Result list created.")

    cursor.close()
    print("[VECTOR-SEARCH-8] Cursor closed.")

    conn.close()
    print("[VECTOR-SEARCH-9] Connection closed.")

    return result


def save_diagnostic_run_history(
    user_question,
    selected_tools,
    knowledge_articles_used,
    diagnostic_context,
    ai_answer,
):
    """
    Saves a DBA Assistant diagnostic run into SQL Server history table.

    This allows the project to keep an audit trail of:
    - The user question
    - Selected diagnostic tools
    - Knowledge Base articles used
    - Diagnostic context
    - Final AI answer
    """

    print("[HISTORY-1] Saving diagnostic run history...")

    query = """
    INSERT INTO dbo.AI_DiagnosticRunHistory
    (
        UserQuestion,
        SelectedTools,
        KnowledgeArticlesUsed,
        DiagnosticContext,
        AIAnswer
    )
    OUTPUT INSERTED.RunID
    VALUES
    (
        ?,
        ?,
        ?,
        ?,
        ?
    );
    """

    with get_connection() as conn:
        print("[HISTORY-2] SQL Server connection opened.")

        cursor = conn.cursor()
        print("[HISTORY-3] Cursor created.")

        cursor.execute(
            query,
            user_question,
            selected_tools,
            knowledge_articles_used,
            diagnostic_context,
            ai_answer,
        )

        run_id = cursor.fetchone()[0]

        conn.commit()
        print(f"[HISTORY-4] Diagnostic run history saved. RunID: {run_id}")

    return run_id