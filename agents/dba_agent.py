
from app.local_embedding import create_local_embedding
from app.db import (
    get_knowledge_base_articles,
    vector_to_sql_json,
    get_relevant_knowledge_articles_by_vector,
)




def build_knowledge_context(articles):
    print("[AGENT-1] Building knowledge context from articles...")

    knowledge_text = ""

    for article in articles:
        knowledge_text += f"""
Title: {article['title']}
Category: {article['category']}
Content: {article['content']}
---
"""

    print("[AGENT-2] Knowledge context was built successfully.")
    return knowledge_text


def build_dba_prompt(user_question):
    print("[AGENT-3] Starting DBA prompt build process...")

    print("[AGENT-4] Loading knowledge base articles from SQL Server...")
    articles = get_knowledge_base_articles()

    print(f"[AGENT-5] Loaded {len(articles)} knowledge base articles.")

    knowledge_context = build_knowledge_context(articles)

    print("[AGENT-6] Building final prompt...")

    prompt = f"""
You are a senior SQL Server DBA assistant.

Your task is to answer the user's question using the DBA knowledge base below.

User question:
{user_question}

DBA knowledge base:
{knowledge_context}

Answer format:
1. Short summary of the problem
2. Possible root causes
3. What to check first
4. Recommended T-SQL queries
5. Risk level
6. Next recommended action

Important rules:
- Answer like a senior SQL Server DBA.
- Be practical and operational.
- If the knowledge base is not enough, say what additional data is needed.
- Do not invent server-specific facts that were not provided.
"""

    print("[AGENT-7] Prompt was built successfully.")
    return prompt



def build_dba_prompt_with_vector_search(user_question, top_n=3):
    print("[AGENT-VECTOR-1] Starting DBA prompt build with vector search...")

    print("[AGENT-VECTOR-2] Creating vector for user question...")
    question_vector = create_local_embedding(user_question)

    print("[AGENT-VECTOR-3] Converting question vector to SQL JSON...")
    question_vector_json = vector_to_sql_json(question_vector)

    print("[AGENT-VECTOR-4] Loading relevant knowledge articles by vector search...")
    relevant_articles = get_relevant_knowledge_articles_by_vector(
        question_vector_json=question_vector_json,
        top_n=top_n,
    )

    print(f"[AGENT-VECTOR-5] Loaded {len(relevant_articles)} relevant articles.")

    knowledge_context = build_knowledge_context(relevant_articles)

    print("[AGENT-VECTOR-6] Building final vector-based prompt...")

    prompt = f"""
You are a senior SQL Server DBA assistant.

Your task is to answer the user's question using only the relevant DBA knowledge base articles below.

User question:
{user_question}

Relevant DBA knowledge base articles:
{knowledge_context}

Answer format:
1. Short summary of the problem
2. Most relevant knowledge base article used
3. Possible root causes
4. What to check first
5. Recommended T-SQL queries
6. Risk level
7. Next recommended action

Important rules:
- Answer like a senior SQL Server DBA.
- Be practical and operational.
- Use only the relevant knowledge provided.
- If the knowledge base is not enough, say what additional data is needed.
- Do not invent server-specific facts that were not provided.
"""

    print("[AGENT-VECTOR-7] Vector-based prompt was built successfully.")
    return prompt


def build_dba_prompt_with_vector_search(user_question, top_n=3):
    print("[AGENT-VECTOR-1] Starting DBA prompt build with vector search...")

    print("[AGENT-VECTOR-2] Creating vector for user question...")
    question_vector = create_local_embedding(user_question)

    print("[AGENT-VECTOR-3] Converting question vector to SQL JSON...")
    question_vector_json = vector_to_sql_json(question_vector)

    print("[AGENT-VECTOR-4] Loading relevant knowledge articles by vector search...")
    relevant_articles = get_relevant_knowledge_articles_by_vector(
        question_vector_json=question_vector_json,
        top_n=top_n,
    )

    print(f"[AGENT-VECTOR-5] Loaded {len(relevant_articles)} relevant articles.")

    knowledge_context = build_knowledge_context(relevant_articles)

    print("[AGENT-VECTOR-6] Building final vector-based prompt...")

    prompt = f"""
You are a senior SQL Server DBA assistant.

Your task is to answer the user's question using only the relevant DBA knowledge base articles below.

User question:
{user_question}

Relevant DBA knowledge base articles:
{knowledge_context}

Answer format:
1. Short summary of the problem
2. Most relevant knowledge base article used
3. Possible root causes
4. What to check first
5. Recommended T-SQL queries
6. Risk level
7. Next recommended action

Important rules:
- Answer like a senior SQL Server DBA.
- Be practical and operational.
- Use only the relevant knowledge provided.
- If the knowledge base is not enough, say what additional data is needed.
- Do not invent server-specific facts that were not provided.
"""

    print("[AGENT-VECTOR-7] Vector-based prompt was built successfully.")
    return prompt