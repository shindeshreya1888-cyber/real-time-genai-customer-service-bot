from .llm import ask_gemini_with_image


image_path = "src/test_image.png"

with open(image_path, "rb") as file:
    image_bytes = file.read()

answer = ask_gemini_with_image(
    "Describe this image. Identify the main object or content you can see.",
    image_bytes,
    "image/png"
)

print("\nGemini image analysis:")
print(answer)