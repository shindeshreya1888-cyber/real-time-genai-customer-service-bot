import os

from langchain_chroma import Chroma
from langchain_core.documents import Document

from .embeddings import create_embeddings
from .loader import load_customer_service_data
from .splitter import split_text


def create_vector_store():
    """
    Create a ChromaDB vector store from the
    customer service knowledge base.
    """

    # Load the customer service document
    text = load_customer_service_data()

    # Split document into chunks
    chunks = split_text(text)

    # Create LangChain Document objects
    documents = [
        Document(
            page_content=chunk,
            metadata={"source": "customer_service.txt"}
        )
        for chunk in chunks
    ]

    # Create embedding model
    embeddings = create_embeddings()

    # Get project root directory
    project_root = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    # ChromaDB storage location
    vector_db_path = os.path.join(
        project_root,
        "vector_db"
    )

    # Create Chroma vector store
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=vector_db_path,
        collection_name="customer_service"
    )

    return vector_store