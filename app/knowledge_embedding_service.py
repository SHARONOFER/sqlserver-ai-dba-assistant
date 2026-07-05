from app.db import get_knowledge_base_articles, save_knowledge_embedding
from app.local_embedding import create_local_embedding


LOCAL_EMBEDDING_MODEL = "local-hash-v1"


def build_knowledge_embedding_text(article):
    print("[KB-EMBED-1] Building text for knowledge article embedding...")

    text = f"""
Title: {article['title']}
Category: {article['category']}
Content: {article['content']}
"""

    print("[KB-EMBED-2] Knowledge article text was built successfully.")
    return text


def generate_embeddings_for_knowledge_base():
    print("[KB-EMBED-3] Starting embeddings generation for knowledge base...")

    print("[KB-EMBED-4] Loading knowledge base articles from SQL Server...")
    articles = get_knowledge_base_articles()

    print(f"[KB-EMBED-5] Loaded {len(articles)} knowledge base articles.")

    saved_count = 0

    for article in articles:
        knowledge_id = article["knowledge_id"]
        title = article["title"]

        print(f"[KB-EMBED-6] Processing KnowledgeID={knowledge_id}, Title={title}")

        embedding_text = build_knowledge_embedding_text(article)

        print(f"[KB-EMBED-7] Creating local embedding for KnowledgeID={knowledge_id}...")
        embedding_vector = create_local_embedding(embedding_text)

        print(f"[KB-EMBED-8] Saving embedding for KnowledgeID={knowledge_id}...")
        save_knowledge_embedding(
            knowledge_id=knowledge_id,
            embedding_model=LOCAL_EMBEDDING_MODEL,
            embedding_vector=embedding_vector,
        )

        saved_count += 1
        print(f"[KB-EMBED-9] Embedding saved for KnowledgeID={knowledge_id}.")

    result = {
        "embedding_model": LOCAL_EMBEDDING_MODEL,
        "articles_processed": len(articles),
        "embeddings_saved": saved_count,
    }

    print("[KB-EMBED-10] Embeddings generation completed successfully.")
    return result