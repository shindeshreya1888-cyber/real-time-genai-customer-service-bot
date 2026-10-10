from .retriever import get_retriever
from .llm import ask_gemini

from .ambiguity_handler import (
    detect_ambiguity,
    build_contextual_question
)

from .response_validator import validate_response
from .sentiment_analyzer import analyze_sentiment
from .language_handler import detect_language


def ask_rag(question, conversation_context=""):

    # ========================================================
    # STEP 1: Get the retriever
    # ========================================================

    retriever = get_retriever()

    # ========================================================
    # STEP 2: Analyze customer sentiment
    # ========================================================

    sentiment_result = analyze_sentiment(question)

    sentiment = sentiment_result["sentiment"]

    # ========================================================
    # STEP 3: Detect customer language
    # ========================================================

    language_result = detect_language(question)

    language_code = language_result["code"]
    language_name = language_result["language"]

    # ========================================================
    # STEP 4: Check whether the question is ambiguous
    # ========================================================

    is_ambiguous = detect_ambiguity(
        question,
        conversation_context
    )

    # ========================================================
    # STEP 5: Create the retrieval question
    # ========================================================

    if is_ambiguous:

        retrieval_question = build_contextual_question(
            question,
            conversation_context
        )

    else:

        retrieval_question = question

    # ========================================================
    # STEP 6: Search the knowledge base
    # ========================================================

    documents = retriever.invoke(
        retrieval_question
    )

    # ========================================================
    # STEP 7: Combine retrieved information
    # ========================================================

    knowledge_context = "\n\n".join(
        document.page_content
        for document in documents
    )

    # ========================================================
    # STEP 8: Create the final prompt
    # ========================================================

    prompt = f"""
You are NovaAssist, a helpful customer service assistant.

Your job is to answer customer questions using the
provided knowledge base and previous conversation.

IMPORTANT RULES:

1. Use the knowledge base as the primary source of
   factual information.

2. Use the previous conversation to understand the
   customer's current question.

3. If the customer uses words such as:
   "it", "this", "that", "they", "my order",
   "how long", or "what about", use the previous
   conversation to understand what they are referring to.

4. Do not invent information.

5. If the knowledge base does not contain enough
   information, say that you do not have enough
   information and recommend contacting customer support.

6. Give a clear, helpful and concise answer.

7. Base the answer on the retrieved knowledge.

8. If the customer is Negative, respond with empathy
   and acknowledge their frustration before providing
   the solution.

9. If the customer is Positive, respond in a friendly
   and appreciative manner.

10. If the customer is Neutral, provide a clear and
    direct answer.

11. Respond in the same language as the customer's
    current message whenever possible.

12. Preserve the customer's intent and conversation
    context even when the customer changes languages.

13. If the customer switches between English, Hindi,
    Marathi, or Spanish, continue understanding the
    conversation correctly.


============================================================
PREVIOUS CONVERSATION
============================================================

{conversation_context}


============================================================
KNOWLEDGE BASE
============================================================

{knowledge_context}


============================================================
CUSTOMER SENTIMENT
============================================================

{sentiment}


============================================================
CUSTOMER LANGUAGE
============================================================

{language_name}


============================================================
CURRENT CUSTOMER QUESTION
============================================================

{question}


============================================================
FINAL ANSWER
============================================================

Answer the customer's current question using the
knowledge base and previous conversation when relevant.
Respond in the customer's detected language.
"""


    # ========================================================
    # STEP 9: Ask Gemini
    # ========================================================

    answer = ask_gemini(prompt)

    # ========================================================
    # STEP 10: Validate the generated answer
    # ========================================================

    validation_result = validate_response(
        answer,
        knowledge_context
    )

    # ========================================================
    # STEP 11: Return answer only if validation succeeds
    # ========================================================

    if validation_result["valid"]:

        return answer

    else:

        return (
            "I could not confidently verify the answer "
            "using the available knowledge base. "
            "Please contact customer support for further assistance."
        )