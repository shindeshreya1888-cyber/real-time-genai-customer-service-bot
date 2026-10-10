from embeddings import create_embeddings


print("=" * 50)
print("Testing Google Embedding Model")
print("=" * 50)

try:

    # Create embedding model
    embeddings = create_embeddings()

    print("\nEmbedding model created successfully!")

    # Test sentence
    text = "Customers can cancel their order before it is shipped."

    print("\nTest sentence:")
    print(text)

    # Convert text into vector
    vector = embeddings.embed_query(text)

    print("\nEmbedding created successfully!")

    print("Vector length:", len(vector))

    print("\nFirst 10 values of the vector:")
    print(vector[:10])

    print("\n" + "=" * 50)
    print("Embedding test completed successfully!")
    print("=" * 50)

except Exception as e:

    print("\nError:")
    print(e)