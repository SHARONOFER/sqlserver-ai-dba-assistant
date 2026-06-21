from app.db import get_connection

def get_top_cpu_procedures(top_n=10):

    """
    Runs a read-only SQL Server DMV query that returns the stored procedures
    with the highest CPU usage from the plan cache.
    """

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

def get_blocking_sessions(top_n=20):
    """
    Runs a read-only SQL Server DMV query that returns sessions
    that are currently blocked by other sessions.
    """

    print("[BLOCKING-1] Starting Blocking Sessions diagnostic tool...")

    query = """
    SELECT TOP (?)
        r.session_id AS blocked_session_id,
        r.blocking_session_id AS blocking_session_id,
        DB_NAME(r.database_id) AS database_name,
        s.login_name AS blocked_login_name,
        s.host_name AS blocked_host_name,
        s.program_name AS blocked_program_name,
        bs.login_name AS blocking_login_name,
        bs.host_name AS blocking_host_name,
        bs.program_name AS blocking_program_name,
        r.status,
        r.command,
        r.wait_type,
        r.wait_time AS wait_time_ms,
        r.wait_resource,
        r.cpu_time,
        r.total_elapsed_time,
        SUBSTRING(
            st.text,
            (r.statement_start_offset / 2) + 1,
            (
                (
                    CASE r.statement_end_offset
                        WHEN -1 THEN DATALENGTH(st.text)
                        ELSE r.statement_end_offset
                    END - r.statement_start_offset
                ) / 2
            ) + 1
        ) AS running_statement_text
    FROM sys.dm_exec_requests r
    INNER JOIN sys.dm_exec_sessions s
        ON r.session_id = s.session_id
    LEFT JOIN sys.dm_exec_sessions bs
        ON r.blocking_session_id = bs.session_id
    OUTER APPLY sys.dm_exec_sql_text(r.sql_handle) st
    WHERE r.blocking_session_id <> 0
    ORDER BY r.wait_time DESC;
    """

    with get_connection() as conn:
        print("[BLOCKING-2] SQL Server connection opened.")

        cursor = conn.cursor()
        print("[BLOCKING-3] Cursor created.")

        cursor.execute(query, top_n)
        print("[BLOCKING-4] Query executed successfully.")

        rows = cursor.fetchall()
        print("[BLOCKING-5] Rows fetched successfully.")

    result = []

    for row in rows:
        result.append(
            {
                "blocked_session_id": row.blocked_session_id,
                "blocking_session_id": row.blocking_session_id,
                "database_name": row.database_name,
                "blocked_login_name": row.blocked_login_name,
                "blocked_host_name": row.blocked_host_name,
                "blocked_program_name": row.blocked_program_name,
                "blocking_login_name": row.blocking_login_name,
                "blocking_host_name": row.blocking_host_name,
                "blocking_program_name": row.blocking_program_name,
                "status": row.status,
                "command": row.command,
                "wait_type": row.wait_type,
                "wait_time_ms": row.wait_time_ms,
                "wait_resource": row.wait_resource,
                "cpu_time": row.cpu_time,
                "total_elapsed_time": row.total_elapsed_time,
                "running_statement_text": row.running_statement_text,
            }
        )

    print("[BLOCKING-6] Diagnostic tool finished successfully.")

    return result