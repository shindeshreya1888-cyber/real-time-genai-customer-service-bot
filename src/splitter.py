from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text):
    """
    Split the document into smaller chunks.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_text(text)

    return chunks