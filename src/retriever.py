import os

from langchain_chroma import Chroma

from .embeddings import create_embeddings


def get_retriever():
    """
    Load the existing ChromaDB vector store
    and create a retriever.
    """

    # Create embedding model
    embeddings = create_embeddings()

    # Find project root directory
    project_root = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    # Location of ChromaDB
    vector_db_path = os.path.join(
        project_root,
        "vector_db"
    )

    # Load existing ChromaDB
    vector_store = Chroma(
        collection_name="customer_service",
        embedding_function=embeddings,
        persist_directory=vector_db_path
    )

    # Create retriever
    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever