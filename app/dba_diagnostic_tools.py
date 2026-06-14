from app.db import get_connection

def get_top_cpu_procedures(top_n=10):
    print("[CPU-PROC-1] Starting Top CPU Procedures diagnostic tool...")

    query = """
    SELECT TOP (?)
        DB_NAME(ps.database_id) AS database_name,
        OBJECT_SCHEMA_NAME(ps.object_id, ps.database_id) AS schema_name,
        OBJECT_NAME(ps.object_id, ps.database_id) AS procedure_name,
        ps.execution_count,
        ps.total_worker_time / 1000 AS total_cpu_ms,
        (ps.total_worker_time / NULLIF(ps.execution_count, 0)) / 1000 AS avg_cpu_ms,
        ps.total_elapsed_time / 1000 AS total_elapsed_ms,
        ps.last_execution_time,
        ps.cached_time
    FROM sys.dm_exec_procedure_stats ps
    WHERE ps.database_id NOT IN (
        DB_ID('master'),
        DB_ID('model'),
        DB_ID('msdb'),
        DB_ID('tempdb')
    )
    ORDER BY ps.total_worker_time DESC;
    """

    connection = get_connection()
    print("[CPU-PROC-2] SQL Server connection opened.")

    cursor = connection.cursor()
    print("[CPU-PROC-3] Cursor created.")

    cursor.execute(query, top_n)
    print("[CPU-PROC-4] Query executed successfully.")

    rows = cursor.fetchall()
    print("[CPU-PROC-5] Rows fetched successfully.")

    results = []

    for row in rows:
        results.append({
            "database_name": row.database_name,
            "schema_name": row.schema_name,
            "procedure_name": row.procedure_name,
            "execution_count": row.execution_count,
            "total_cpu_ms": row.total_cpu_ms,
            "avg_cpu_ms": row.avg_cpu_ms,
            "total_elapsed_ms": row.total_elapsed_ms,
            "last_execution_time": row.last_execution_time,
            "cached_time": row.cached_time,
        })

    cursor.close()
    connection.close()

    print("[CPU-PROC-6] Diagnostic tool finished successfully.")

    return results