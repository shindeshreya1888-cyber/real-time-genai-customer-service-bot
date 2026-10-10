
from .medical_retriever import retrieve_medical_information
from .medical_entities import extract_medical_entities


def ask_medical(question):
    """
    Retrieve relevant medical information and extract
    diseases, symptoms, and treatments from the question.
    """

    if not question or not question.strip():
        return {
            "answer": "Please enter a medical question.",
            "entities": {
                "diseases": [],
                "symptoms": [],
                "treatments": []
            }
        }

    # Step 1: Retrieve relevant medical records
    results = retrieve_medical_information(question)

    # Step 2: Extract medical entities from the question
    entities = extract_medical_entities(question)

    # Step 3: Handle questions with no matching information
    if not results:
        return {
            "answer": (
                "I could not find relevant information in "
                "the medical knowledge base. Please consult "
                "a qualified healthcare professional."
            ),
            "entities": entities
        }

    # Step 4: Format the retrieved answers
    answer_parts = []

    for index, record in enumerate(results, start=1):
        answer_parts.append(
            f"Result {index}\n"
            f"Related question: {record['question']}\n"
            f"Information: {record['answer']}"
        )

    answer = (
        "Medical information retrieved from the MedQuAD dataset:\n\n"
        + "\n\n".join(answer_parts)
        + "\n\nDetected medical entities:\n"
        + f"Diseases: {', '.join(entities['diseases']) or 'None detected'}\n"
        + f"Symptoms: {', '.join(entities['symptoms']) or 'None detected'}\n"
        + f"Treatments: {', '.join(entities['treatments']) or 'None detected'}\n\n"
        + "Disclaimer: This information is for educational purposes "
        + "only and is not a diagnosis or a substitute for advice "
        + "from a qualified healthcare professional."
    )

    return {
        "answer": answer,
        "entities": entities
    }
