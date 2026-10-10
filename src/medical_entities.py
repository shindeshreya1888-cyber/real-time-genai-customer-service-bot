
import re


MEDICAL_TERMS = {
    "diseases": [
        "diabetes",
        "hypertension",
        "asthma",
        "anemia",
        "cancer",
        "arthritis",
        "pneumonia",
        "migraine",
        "lymphocytic choriomeningitis",
        "chronic lymphocytic leukemia",
        "heart disease",
        "kidney disease"
    ],
    "symptoms": [
        "fever",
        "cough",
        "fatigue",
        "headache",
        "dizziness",
        "wheezing",
        "shortness of breath",
        "chest pain",
        "chest tightness",
        "weight loss",
        "frequent urination",
        "increased thirst",
        "nausea",
        "vomiting",
        "diarrhea",
        "rash"
    ],
    "treatments": [
        "insulin",
        "medication",
        "medications",
        "medicine",
        "medicines",
        "inhaler",
        "inhalers",
        "therapy",
        "surgery",
        "chemotherapy",
        "radiation therapy",
        "antibiotics",
        "lifestyle changes",
        "blood glucose monitoring"
    ]
}


def extract_medical_entities(text):
    """
    Identify known disease, symptom, and treatment terms.

    This is a simple dictionary-based extractor, not a
    full medical diagnosis or advanced NLP model.
    """

    text_lower = text.lower()
    extracted = {}

    for category, terms in MEDICAL_TERMS.items():
        matches = []

        for term in terms:
            pattern = r"(?<!\w)" + re.escape(term) + r"(?!\w)"

            if re.search(pattern, text_lower):
                matches.append(term)

        extracted[category] = matches

    return extracted