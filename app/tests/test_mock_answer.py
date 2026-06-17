from agents.dba_agent import generate_mock_dba_answer


user_question = "High CPU on SQL Server"

answer = generate_mock_dba_answer(
    user_question=user_question,
    top_n=1
)

print(answer)