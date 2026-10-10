from vector_store import create_vector_store


print("=" * 50)
print("Testing ChromaDB Vector Store")
print("=" * 50)

try:

    # Create vector store
    vector_store = create_vector_store()

    print("\nVector store created successfully!")

    # Test similarity search
    question = "How can I cancel my order?"

    print("\nTest question:")
    print(question)

    results = vector_store.similarity_search(
        question,
        k=3
    )

    print("\nRelevant documents found:", len(results))

    print("\n" + "=" * 50)
    print("SEARCH RESULTS")
    print("=" * 50)

    for i, result in enumerate(results, start=1):

        print(f"\nResult {i}:")
        print(result.page_content)

    print("\n" + "=" * 50)
    print("ChromaDB test completed successfully!")
    print("=" * 50)

except Exception as e:

    print("\nError:")
    print(e)