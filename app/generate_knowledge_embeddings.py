from app.knowledge_embedding_service import generate_embeddings_for_knowledge_base


def main():
    """
    Maintenance entry point.
    Generates or refreshes embeddings for all knowledge base articles
    stored in SQL Server.
    """

    generate_embeddings_for_knowledge_base()


if __name__ == "__main__":
    main()