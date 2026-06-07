from agents.dba_agent import generate_mock_dba_answer


def main():
    print("SQL Server AI DBA Assistant")
    print("---------------------------")

    user_question = input("Enter your DBA question: ")

    answer = generate_mock_dba_answer(
        user_question=user_question,
        top_n=1
    )

    print(answer)


if __name__ == "__main__":
    main()