from retriever import get_retriever


print("=" * 50)
print("Testing Retriever")
print("=" * 50)

try:

    # Create retriever
    retriever = get_retriever()

    print("\nRetriever created successfully!")

    # Customer question
    question = "How can I cancel my order?"

    print("\nCustomer question:")
    print(question)

    # Search for relevant information
    documents = retriever.invoke(question)

    print("\nRelevant documents found:", len(documents))

    print("\n" + "=" * 50)
    print("RETRIEVED INFORMATION")
    print("=" * 50)

    for i, document in enumerate(documents, start=1):

        print(f"\nResult {i}:")
        print(document.page_content)

    print("\n" + "=" * 50)
    print("Retriever test completed successfully!")
    print("=" * 50)

except Exception as e:

    print("\nError:")
    print(e)