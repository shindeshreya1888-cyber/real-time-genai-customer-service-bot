import os
import requests

url = "https://raw.githubusercontent.com/abachaa/MedQuAD/master/ori_dataset.json"

project_root = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

output_folder = os.path.join(
    project_root,
    "data",
    "medical"
)

os.makedirs(output_folder, exist_ok=True)

output_file = os.path.join(
    output_folder,
    "medquad.json"
)

print("Downloading MedQuAD dataset...")

response = requests.get(url, timeout=60)

if response.status_code != 200:
    print("Download failed.")
    print("Status code:", response.status_code)
    print(response.text[:500])
else:
    with open(output_file, "wb") as file:
        file.write(response.content)

    print("MedQuAD dataset downloaded successfully.")
    print("Saved to:")
    print(output_file)
    print("File size:", len(response.content), "bytes")