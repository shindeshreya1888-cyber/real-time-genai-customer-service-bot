from .retriever import get_retriever


print("=" * 60)
print("       Testing RAG Retrieval Without Gemini")
print("=" * 60)


retriever = get_retriever()


questions = [
    "What is the refund policy?",
    "How can I contact customer support?",
    "How can I cancel my order?"
]


for question in questions:

    print("\n" + "=" * 60)

    print("\nCustomer Question:")
    print(question)

    documents = retriever.invoke(question)

    print("\nRetrieved Information:")

    for i, document in enumerate(documents, start=1):

        print(f"\n--- Result {i} ---")
        print(document.page_content)


print("\n" + "=" * 60)
print("Retrieval test completed successfully!")
print("=" * 60)