
import re


def summarize_paper(abstract, max_sentences=3):
    """
    Create a simple extractive summary from a research abstract.
    Selects the first few sentences without using an external API.
    """

    if not abstract or not abstract.strip():
        return "No abstract is available to summarize."

    # Clean extra whitespace
    abstract = " ".join(abstract.split())

    # Split the abstract into sentences
    sentences = re.split(r'(?<=[.!?])\s+', abstract)

    # Remove empty sentences
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    if not sentences:
        return "Unable to summarize this abstract."

    selected_sentences = sentences[:max_sentences]

    return " ".join(selected_sentences)
