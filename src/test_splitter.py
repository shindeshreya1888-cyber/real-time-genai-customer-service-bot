from loader import load_customer_service_data
from splitter import split_text


print("=" * 50)
print("Testing Text Splitter")
print("=" * 50)

try:

    # Load the customer service document
    text = load_customer_service_data()

    print("\nDocument loaded successfully.")
    print("Original document length:", len(text), "characters")

    # Split the document
    chunks = split_text(text)

    print("Number of chunks created:", len(chunks))

    print("\n" + "=" * 50)
    print("FIRST CHUNK")
    print("=" * 50)

    print(chunks[0])

    print("\n" + "=" * 50)
    print("SECOND CHUNK")
    print("=" * 50)

    if len(chunks) > 1:
        print(chunks[1])

    print("\n" + "=" * 50)
    print("Text splitter test completed successfully!")
    print("=" * 50)

except Exception as e:

    print("\nError:")
    print(e)