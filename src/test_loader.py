from loader import load_customer_service_data


print("=" * 50)
print("Testing Customer Service Document Loader")
print("=" * 50)

try:

    data = load_customer_service_data()

    print("\nDocument loaded successfully!")
    print("\nFirst 1000 characters of the document:\n")
    print(data[:1000])

    print("\n" + "=" * 50)
    print("Loader test completed successfully!")
    print("=" * 50)

except Exception as e:

    print("\nError loading document:")
    print(e)