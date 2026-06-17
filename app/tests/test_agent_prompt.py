from agents.dba_agent import build_dba_prompt_with_vector_search


user_question = "High CPU on SQL Server"

prompt = build_dba_prompt_with_vector_search(
    user_question=user_question,
    top_n=1
)

print(prompt)