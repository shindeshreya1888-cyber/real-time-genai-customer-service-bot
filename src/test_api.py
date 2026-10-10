import os
import sys

# Allow Python to find files inside src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
from llm import llm

# Load environment variables
load_dotenv()

# Check API key
print("API KEY FOUND:", bool(os.getenv("GOOGLE_API_KEY")))

print("Sending test message to Gemini...")

response = llm.invoke("Say hello in one short sentence.")

print("Gemini response:")
print(response.content)