from app.db import test_connection


def main():
    print("[MAIN-1] Application started.")
    print("[MAIN-2] Starting SQL Server connection test...")

    result = test_connection()

    print("[MAIN-3] SQL Server connection test completed successfully.")
    print("[MAIN-4] Connection details:")

    print(f"Server Name:   {result['server_name']}")
    print(f"Database Name: {result['database_name']}")
    print(f"Login Name:    {result['login_name']}")
    print(f"System User:   {result['system_user']}")

    print("[MAIN-5] Application finished successfully.")


if __name__ == "__main__":
    main()