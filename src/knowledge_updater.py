import os
import hashlib

from langchain_chroma import Chroma
from langchain_core.documents import Document

from .embeddings import create_embeddings
from .splitter import split_text


def get_project_root():
    """
    Get the root folder of the project.
    """

    return os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )


def get_source_folder():
    """
    Get the folder containing dynamic knowledge sources.
    """

    project_root = get_project_root()

    return os.path.join(
        project_root,
        "data",
        "sources"
    )


def get_vector_db_path():
    """
    Get the ChromaDB folder.
    """

    project_root = get_project_root()

    return os.path.join(
        project_root,
        "vector_db"
    )


def calculate_file_hash(file_path):
    """
    Create a unique hash for the file contents.

    This allows us to detect whether
    a source has changed.
    """

    with open(file_path, "rb") as file:

        file_content = file.read()

    return hashlib.sha256(file_content).hexdigest()


def get_vector_store():
    """
    Load the existing ChromaDB vector store.
    """

    embeddings = create_embeddings()

    vector_store = Chroma(
        collection_name="customer_service",
        embedding_function=embeddings,
        persist_directory=get_vector_db_path()
    )

    return vector_store


def update_file(file_path):
    """
    Add or update one knowledge-base file
    inside ChromaDB.
    """

    file_name = os.path.basename(file_path)

    print(f"\nChecking source: {file_name}")

    file_hash = calculate_file_hash(file_path)

    vector_store = get_vector_store()

    # Check whether this source already exists
    existing_data = vector_store.get(
        where={"source": file_name}
    )

    existing_ids = existing_data.get("ids", [])

    # If the source already exists, remove its old chunks
    if existing_ids:

        print(f"Existing information found for {file_name}")

        print("Removing old chunks...")

        vector_store.delete(
            ids=existing_ids
        )

    # Read the new source
    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        text = file.read()

    if not text.strip():

        print(f"No information found in {file_name}")

        return

    # Split the new information
    chunks = split_text(text)

    documents = []

    ids = []

    for index, chunk in enumerate(chunks):

        document = Document(
            page_content=chunk,
            metadata={
                "source": file_name,
                "file_hash": file_hash,
                "chunk": index
            }
        )

        documents.append(document)

        ids.append(
            f"{file_name}_{file_hash[:12]}_{index}"
        )

    # Add new information
    vector_store.add_documents(
        documents=documents,
        ids=ids
    )

    print(
        f"Updated {file_name} "
        f"with {len(documents)} chunks."
    )


def update_knowledge_base():
    """
    Check all source files and update ChromaDB.
    """

    print("\n" + "=" * 60)

    print("Starting knowledge-base update...")

    print("=" * 60)

    source_folder = get_source_folder()

    if not os.path.exists(source_folder):

        print(
            "Source folder does not exist:",
            source_folder
        )

        return

    files = [
        file_name
        for file_name in os.listdir(source_folder)
        if file_name.endswith(".txt")
    ]

    if not files:

        print("No source files found.")

        return

    for file_name in files:

        file_path = os.path.join(
            source_folder,
            file_name
        )

        try:

            update_file(file_path)

        except Exception as error:

            print(
                f"Error updating {file_name}:"
            )

            print(error)

    print("\nKnowledge-base update completed.")

    print("=" * 60)