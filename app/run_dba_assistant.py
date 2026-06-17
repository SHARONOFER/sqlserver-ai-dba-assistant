from agents.dba_agent import generate_real_dba_answer


def main():
    print("SQL Server AI DBA Assistant")
    print("---------------------------")

    user_question = input("User question:\n")

    answer = generate_real_dba_answer(
        user_question=user_question,
        top_n=3
    )

    print("\nAI DBA Answer:")
    print("--------------")
    print(answer)


if __name__ == "__main__":
    main()