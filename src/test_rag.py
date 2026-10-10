from rag import ask_rag


print("=" * 60)
print("        Testing RAG Customer Service Bot")
print("=" * 60)


questions = [
    "How can I cancel my order?",
    "What is the refund policy?",
    "How can I contact customer support?"
]


for question in questions:

    print("\n" + "=" * 60)

    print("\nCustomer:")
    print(question)

    try:

        answer = ask_rag(question)

        print("\nBot:")
        print(answer)

    except Exception as e:

        print("\nError:")
        print(e)


print("\n" + "=" * 60)
print("RAG test completed!")
print("=" * 60)