
import os
import base64

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError(
        "GOOGLE_API_KEY was not found. Please check your .env file."
    )

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=api_key
)


def ask_gemini(question):
    """
    Send a text question to Gemini and return the response.
    """

    if not isinstance(question, str) or not question.strip():
        raise ValueError("Please enter a valid question.")

    response = llm.invoke(question)
    content = response.content

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_parts = []

        for part in content:
            if isinstance(part, dict):
                text_value = part.get("text", "")
                if text_value:
                    text_parts.append(text_value)
            elif isinstance(part, str):
                text_parts.append(part)

        return "\n".join(text_parts)

    return str(content)


def ask_gemini_with_image(question, image_bytes, mime_type):
    """
    Send a text question and an uploaded image to Gemini.
    Supports JPEG, PNG, and WEBP images.
    """

    # Step 1: Validate the question
    if not isinstance(question, str) or not question.strip():
        raise ValueError("Please enter a question about the image.")

    # Step 2: Validate image data
    if not isinstance(image_bytes, bytes) or not image_bytes:
        raise ValueError("The uploaded image is empty or invalid.")

    # Step 3: Validate image format
    supported_types = {
        "image/jpeg",
        "image/png",
        "image/webp"
    }

    if mime_type not in supported_types:
        raise ValueError(
            "Unsupported image format. Please upload a JPG, PNG, or WEBP image."
        )

    # Step 4: Limit image size to 10 MB
    max_size = 10 * 1024 * 1024

    if len(image_bytes) > max_size:
        raise ValueError(
            "The image is too large. Please upload an image smaller than 10 MB."
        )

    # Step 5: Encode image as Base64
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    image_data_url = (
        f"data:{mime_type};base64,{image_base64}"
    )

    # Step 6: Send the question and image to Gemini
    response = llm.invoke([
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": question
                },
                {
                    "type": "image_url",
                    "image_url": image_data_url
                }
            ]
        }
    ])

    # Step 7: Extract the response text
    content = response.content

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_parts = []

        for part in content:
            if isinstance(part, dict):
                text_value = part.get("text", "")
                if text_value:
                    text_parts.append(text_value)
            elif isinstance(part, str):
                text_parts.append(part)

        return "\n".join(text_parts)

    return str(content)
