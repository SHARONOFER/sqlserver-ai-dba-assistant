from app.dba_diagnostic_tools import get_top_cpu_procedures


def main():
    results = get_top_cpu_procedures(top_n=5)

    print("\nTop CPU Stored Procedures:")
    print("--------------------------")

    for index, item in enumerate(results, start=1):
        print(f"\n#{index}")
        print(f"Database: {item['database_name']}")
        print(f"Schema: {item['schema_name']}")
        print(f"Procedure: {item['procedure_name']}")
        print(f"Execution count: {item['execution_count']}")
        print(f"Total CPU ms: {item['total_cpu_ms']}")
        print(f"Avg CPU ms: {item['avg_cpu_ms']}")
        print(f"Total elapsed ms: {item['total_elapsed_ms']}")
        print(f"Last execution: {item['last_execution_time']}")
        print(f"Cached time: {item['cached_time']}")


if __name__ == "__main__":
    main()