from src.rag import ask_rag


print("=" * 60)
print("        GenAI Customer Service RAG Bot")
print("=" * 60)

print("\nType 'exit' to close the chatbot.")

while True:

    user_input = input("\nYou: ")

    # Exit commands
    if user_input.lower() in ["exit", "quit", "bye"]:

        print("\nBot: Thank you for contacting us. Goodbye!")

        break

    # Ignore empty questions
    if not user_input.strip():
        continue

    try:

        # Send question to RAG system
        response = ask_rag(user_input)

        print("\nBot:")
        print(response)

    except Exception as e:

        print("\nBot: Sorry, I was unable to process your request.")

        print("\nError:")
        print(e)