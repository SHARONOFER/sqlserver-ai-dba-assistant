from app.dba_diagnostic_tools import get_blocking_sessions


def test_get_blocking_sessions():
    blocking_sessions = get_blocking_sessions(top_n=20)

    assert isinstance(blocking_sessions, list)

    print("\nBlocking Sessions:")
    print("------------------")

    if not blocking_sessions:
        print("No blocking sessions found.")
        return

    for item in blocking_sessions:
        print(f"Blocked session: {item['blocked_session_id']}")
        print(f"Blocking session: {item['blocking_session_id']}")
        print(f"Database: {item['database_name']}")
        print(f"Wait type: {item['wait_type']}")
        print(f"Wait time ms: {item['wait_time_ms']}")
        print(f"Statement: {item['running_statement_text']}")
        print("---")


if __name__ == "__main__":
    test_get_blocking_sessions()

    print("\nBlocking sessions tool test finished successfully.")