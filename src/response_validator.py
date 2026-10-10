def validate_response(answer, knowledge_context):
    """
    Performs a simple evidence-based validation of the
    chatbot's response.

    The function checks whether important words from the
    retrieved knowledge appear in the generated answer.
    """

    # --------------------------------------------------------
    # Basic safety checks
    # --------------------------------------------------------

    if not answer:
        return {
            "valid": False,
            "reason": "The chatbot returned an empty response."
        }

    if not knowledge_context:
        return {
            "valid": False,
            "reason": "No supporting knowledge was retrieved."
        }


    # --------------------------------------------------------
    # Convert text to lowercase
    # --------------------------------------------------------

    answer_lower = answer.lower()
    knowledge_lower = knowledge_context.lower()


    # --------------------------------------------------------
    # Extract useful words from the knowledge
    # --------------------------------------------------------

    knowledge_words = set(
        word.strip(".,!?():;\"'")
        for word in knowledge_lower.split()
        if len(word.strip(".,!?():;\"'")) > 4
    )


    # --------------------------------------------------------
    # Find knowledge words present in the answer
    # --------------------------------------------------------

    matching_words = [
        word
        for word in knowledge_words
        if word in answer_lower
    ]


    # --------------------------------------------------------
    # Calculate simple evidence score
    # --------------------------------------------------------

    if len(knowledge_words) == 0:

        return {
            "valid": False,
            "reason": "Unable to identify evidence words."
        }


    evidence_score = (
        len(matching_words) / len(knowledge_words)
    )


    # --------------------------------------------------------
    # Validation decision
    # --------------------------------------------------------

    if len(matching_words) >= 3:

        return {
            "valid": True,
            "reason": "The response contains information supported by the retrieved knowledge.",
            "evidence_score": round(evidence_score, 3)
        }


    # --------------------------------------------------------
    # Unsafe / unsupported response
    # --------------------------------------------------------

    return {
        "valid": False,
        "reason": "The response does not contain enough evidence from the retrieved knowledge.",
        "evidence_score": round(evidence_score, 3)
    }