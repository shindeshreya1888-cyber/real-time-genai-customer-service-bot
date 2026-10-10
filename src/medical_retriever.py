
import csv
import os
import re


def load_medical_data():
    """Load medical questions and answers from the local CSV file."""

    project_root = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    file_path = os.path.join(
        project_root,
        "data",
        "medical",
        "medquad.csv"
    )

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Medical dataset not found: {file_path}"
        )

    records = []

    with open(file_path, "r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            question = (row.get("question") or "").strip()
            answer = (row.get("answer") or "").strip()
            qtype = (row.get("qtype") or "").strip()

            if question and answer:
                records.append({
                    "question": question,
                    "answer": answer,
                    "qtype": qtype
                })

    return records


def tokenize(text):
    """Convert text into lowercase searchable words."""

    return re.findall(r"\b[a-zA-Z0-9]+\b", text.lower())


def retrieve_medical_information(question, top_k=3):
    """Find the most relevant medical Q&A records using word overlap."""

    records = load_medical_data()
    query_words = set(tokenize(question))

    if not query_words:
        return []

    scored_records = []

    for record in records:
        question_words = set(tokenize(record["question"]))
        answer_words = set(tokenize(record["answer"]))

        # Give more importance to matches in the question itself.
        question_matches = len(query_words & question_words)
        answer_matches = len(query_words & answer_words)

        score = (question_matches * 3) + answer_matches

        if score > 0:
            scored_records.append((score, record))

    scored_records.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [
        record
        for score, record in scored_records[:top_k]
    ]