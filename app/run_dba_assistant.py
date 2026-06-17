from agents.dba_agent import generate_real_dba_answer


def main():

    """
    Entry point of the DBA assistant application.
    Reads the user's DBA question, sends it to the agent,
    and prints the final AI-generated DBA answer.
    """

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