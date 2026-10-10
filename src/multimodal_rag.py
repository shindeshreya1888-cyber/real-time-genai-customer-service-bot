from .retriever import get_retriever
from .llm import ask_gemini_with_image


def ask_multimodal_rag(
    question,
    image_bytes,
    mime_type,
    conversation_context=""
):
    """
    Combines:
    1. User question
    2. Uploaded image
    3. Conversation memory
    4. Knowledge-base retrieval

    Then sends all relevant information to Gemini
    for a contextual answer.
    """

    # =========================================================
    # STEP 1: Get the retriever
    # =========================================================

    retriever = get_retriever()


    # =========================================================
    # STEP 2: Search the knowledge base
    # =========================================================

    documents = retriever.invoke(question)


    # =========================================================
    # STEP 3: Combine retrieved information
    # =========================================================

    knowledge_context = "\n\n".join(
        document.page_content
        for document in documents
    )


    # =========================================================
    # STEP 4: Create multimodal prompt
    # =========================================================

    prompt = f"""
You are NovaAssist, an intelligent customer service assistant.

You are capable of understanding both text and images.

Your task is to analyze the uploaded image together with
the customer's question, previous conversation, and
retrieved knowledge-base information.

IMPORTANT RULES:

1. Carefully analyze the uploaded image.

2. Use the knowledge base as the primary source for
   customer-service policies and factual information.

3. Use the previous conversation to understand context.

4. If the customer refers to something using words such as
   "it", "this", "that", "my order", or "this image",
   use the previous conversation and image information
   to understand what they mean.

5. Do not invent information that is not present in the
   image, conversation, or knowledge base.

6. If the image does not contain enough information,
   clearly say what information is missing.

7. If the knowledge base does not contain enough information,
   recommend contacting customer support.

8. Give a concise and helpful answer.

9. Clearly distinguish between information observed in
   the image and information obtained from the knowledge base.

10. Do not make assumptions about information that cannot
    be seen or retrieved.


============================================================
PREVIOUS CONVERSATION
============================================================

{conversation_context}


============================================================
KNOWLEDGE BASE INFORMATION
============================================================

{knowledge_context}


============================================================
CUSTOMER QUESTION
============================================================

{question}


============================================================
TASK
============================================================

Analyze the uploaded image and answer the customer's
question using:

- The uploaded image
- The previous conversation
- The retrieved knowledge base

Provide an evidence-based customer-service response.
"""


    # =========================================================
    # STEP 5: Send image + prompt to Gemini
    # =========================================================

    answer = ask_gemini_with_image(
        prompt,
        image_bytes,
        mime_type
    )


    return answer