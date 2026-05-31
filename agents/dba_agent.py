from app.db import get_knowledge_base_articles


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