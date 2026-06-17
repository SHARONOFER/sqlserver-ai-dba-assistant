from app.db import test_connection, get_table_counts


def main():
    print("[MAIN-1] Application started.")

    print("[MAIN-2] Starting SQL Server connection test...")
    connection_result = test_connection()

    print("[MAIN-3] SQL Server connection test completed successfully.")
    print("[MAIN-4] Connection details:")
    print(f"Server Name:   {connection_result['server_name']}")
    print(f"Database Name: {connection_result['database_name']}")
    print(f"Login Name:    {connection_result['login_name']}")
    print(f"System User:   {connection_result['system_user']}")

    print("[MAIN-5] Starting table counts query...")   
    table_counts = get_table_counts()

    print("[MAIN-6] Table counts result:")
    for item in table_counts:
        print(f"{item['table_name']}: {item['row_count']} rows")

    print("[MAIN-7] Application finished successfully.")


if __name__ == "__main__":
    main()