def detect_ambiguity(question, conversation_context):
    """
    Detects whether a question contains words that may
    require previous conversation context.
    """

    ambiguous_words = [
        "it",
        "this",
        "that",
        "they",
        "them",
        "these",
        "those",
        "he",
        "she",
        "how long",
        "what about",
        "what is it",
        "same",
        "again"
    ]

    question_lower = question.lower()

    for word in ambiguous_words:

        if word in question_lower:

            if conversation_context:
                return True

    return False


def build_contextual_question(
    question,
    conversation_context
):
    """
    Creates a question containing previous conversation
    so the RAG system can understand references.
    """

    if not conversation_context:
        return question

    contextual_question = f"""
Previous conversation:

{conversation_context}


Current customer question:

{question}


Rewrite the current question mentally using the
previous conversation so that references such as
"it", "this", "that", "they", "how long", or
"what about" are understood correctly.

Return the meaning of the customer's current question.
"""

    return contextual_question