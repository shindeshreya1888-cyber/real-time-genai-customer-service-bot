from src.llm import ask_gemini
import time


print("=" * 50)
print("        GenAI Customer Service Bot")
print("=" * 50)


while True:

    user_input = input("\nYou: ")

    # Exit commands
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Bot: Thank you for contacting us. Goodbye!")
        break

    # Ignore empty input
    if not user_input.strip():
        continue

    # Try Gemini up to 3 times
    for attempt in range(3):

        try:
            response = ask_gemini(user_input)

            print("Bot:", response)

            break

        except Exception as e:

            error_message = str(e)

            # Retry temporary 503 errors
            if "503" in error_message or "UNAVAILABLE" in error_message:

                if attempt < 2:
                    print("Bot: Gemini is temporarily busy. Retrying...")
                    time.sleep(3)
                else:
                    print("Bot: Gemini is currently busy. Please try again in a moment.")

            else:
                print("Error:", error_message)
                break