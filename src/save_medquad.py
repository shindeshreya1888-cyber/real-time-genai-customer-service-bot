import os
import csv

from datasets import load_dataset


print("=" * 60)
print("Loading MedQuAD dataset...")
print("=" * 60)

dataset = load_dataset(
    "prithvi1029/medquad-medical-qa"
)

train_data = dataset["train"]

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
    "medquad.csv"
)

with open(
    output_file,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "qtype",
        "question",
        "answer"
    ])

    for record in train_data:

        writer.writerow([
            record["qtype"],
            record["Question"],
            record["Answer"]
        ])

print("\nMedQuAD dataset saved successfully.")
print("Number of records:", len(train_data))
print("Saved to:")
print(output_file)