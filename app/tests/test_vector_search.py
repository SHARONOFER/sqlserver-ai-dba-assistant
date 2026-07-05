from app.local_embedding import create_local_embedding
from app.db import vector_to_sql_json, get_relevant_knowledge_articles_by_vector


user_question = "High CPU on SQL Server"

print("[TEST-1] Creating vector for user question...")
question_vector = create_local_embedding(user_question)

print("[TEST-2] Converting vector to SQL JSON...")
question_vector_json = vector_to_sql_json(question_vector)

print("[TEST-3] Running vector search...")
results = get_relevant_knowledge_articles_by_vector(question_vector_json, top_n=3)

print("[TEST-4] Results:")
for item in results:
    print(
        item["knowledge_id"],
        item["title"],
        item["distance"]
    )