from langdetect import detect, DetectorFactory

# Make language detection consistent
DetectorFactory.seed = 0


LANGUAGE_NAMES = {
    "en": "English",
    "hi": "Hindi",
    "mr": "Marathi",
    "es": "Spanish",
    "fr": "French",
    "de": "German"
}


def detect_language(text):
    """
    Detect the language of the user's message.

    Returns:
        language code
        language name
    """

    if not text or not text.strip():
        return {
            "code": "unknown",
            "language": "Unknown"
        }

    try:
        language_code = detect(text)

        language_name = LANGUAGE_NAMES.get(
            language_code,
            language_code
        )

        return {
            "code": language_code,
            "language": language_name
        }

    except Exception:
        return {
            "code": "unknown",
            "language": "Unknown"
        }