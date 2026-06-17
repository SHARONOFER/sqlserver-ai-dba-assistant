
from app.dba_diagnostic_tools import get_top_cpu_procedures

from app.ai_client import generate_ai_response

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



def build_dba_prompt_with_vector_search(user_question, top_n=1):
    print("[AGENT-VECTOR-1] Starting DBA prompt build with vector search...")

    print("[AGENT-VECTOR-2] Creating vector for user question...")
    question_vector = create_local_embedding(user_question) 

    print("[AGENT-VECTOR-3] Converting question vector to SQL JSON...")
    question_vector_json = vector_to_sql_json(question_vector) 

    print("[AGENT-VECTOR-4] Loading relevant knowledge articles by vector search...")
    relevant_articles = get_relevant_knowledge_articles_by_vector     (
        question_vector_json=question_vector_json,
        top_n=top_n,
    )

    print(f"[AGENT-VECTOR-5] Loaded {len(relevant_articles)} relevant articles.")

    knowledge_context = build_knowledge_context(relevant_articles) 

    cpu_diagnostic_context = "CPU diagnostics were not executed."

  
    if should_run_cpu_diagnostics(user_question):
        print("[AGENT-CPU-3] CPU question detected. Running CPU diagnostic tool...")
        cpu_procedures = get_top_cpu_procedures(top_n=5)
        cpu_diagnostic_context = build_cpu_diagnostic_context(cpu_procedures)
    else:
        print("[AGENT-CPU-4] CPU diagnostic tool was not needed.")

    print("[AGENT-VECTOR-6] Building final vector-based prompt...")

    prompt = f"""
You are a senior SQL Server DBA assistant.

Your task is to answer the user's question using the relevant DBA knowledge base articles and the real SQL Server diagnostic data below.

User question:
{user_question}


Relevant DBA knowledge base articles:
{knowledge_context}

Real SQL Server diagnostic data:
{cpu_diagnostic_context}




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


def generate_mock_dba_answer(user_question, top_n=1):
    print("[MOCK-ANSWER-1] Starting mock DBA answer generation...")

    print("[MOCK-ANSWER-2] Getting relevant knowledge using vector search...")
    prompt = build_dba_prompt_with_vector_search(
        user_question=user_question,
        top_n=top_n,
    )

    answer = f"""
MOCK DBA ANSWER

User question:
{user_question}

This is not a real AI response yet.
At this stage, the system successfully:
1. Received the user question
2. Found relevant DBA knowledge using vector search
3. Built a DBA prompt from the relevant knowledge

The prompt that would be sent to the AI model is:

{prompt}
"""

    print("[MOCK-ANSWER-3] Mock DBA answer generated successfully.")
    return answer




def build_cpu_diagnostic_context(cpu_procedures):
    print("[AGENT-CPU-1] Building CPU diagnostic context...")

    if not cpu_procedures:
        return "No CPU diagnostic data was returned from SQL Server."

    lines = []
    for item in cpu_procedures:
        if (
            item["database_name"] is None
            or item["schema_name"] is None
            or item["procedure_name"] is None
        ):
            continue

        lines.append(
            f"Database: {item['database_name']}\n"
            f"Schema: {item['schema_name']}\n"
            f"Procedure: {item['procedure_name']}\n"
            f"Execution count: {item['execution_count']}\n"
            f"Total CPU ms: {item['total_cpu_ms']}\n"
            f"Average CPU ms: {item['avg_cpu_ms']}\n"
            f"Total elapsed ms: {item['total_elapsed_ms']}\n"
            f"Last execution time: {item['last_execution_time']}\n"
            f"Cached time: {item['cached_time']}\n"
            "---"
        )
        

    print("[AGENT-CPU-2] CPU diagnostic context was built successfully.")

    return "\n".join(lines)



def should_run_cpu_diagnostics(user_question):
    question_lower = user_question.lower()

    cpu_keywords = [
        "cpu",
        "high cpu",
        "processor",
        "slow server",
        "performance"
    ]

    return any(keyword in question_lower for keyword in cpu_keywords)




def generate_real_dba_answer(user_question, top_n=1):
    print("[REAL-ANSWER-1] Starting real DBA answer generation...")

    print("[REAL-ANSWER-2] Building vector-based DBA prompt...")
    prompt = build_dba_prompt_with_vector_search(
        user_question=user_question,
        top_n=top_n
    )

    print("\n========== PROMPT SENT TO GEMINI ==========")
    print(prompt)
    print("========== END PROMPT ==========\n")

    print("[REAL-ANSWER-3] Sending prompt to Gemini AI...")
    answer = generate_ai_response(prompt)

    print("[REAL-ANSWER-4] Real DBA answer received from Gemini.")

    return answer