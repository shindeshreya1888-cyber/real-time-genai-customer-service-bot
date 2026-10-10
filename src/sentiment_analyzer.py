def analyze_sentiment(text):
    """
    Simple local sentiment analyzer for customer messages.

    Returns:
        Positive, Negative, or Neutral
    """

    positive_words = [
        "good",
        "great",
        "excellent",
        "happy",
        "thanks",
        "thank",
        "thank you",
        "amazing",
        "helpful",
        "love",
        "satisfied",
        "perfect",
        "awesome",
        "quick",
        "fast"
    ]

    negative_words = [
        "bad",
        "terrible",
        "worst",
        "angry",
        "unhappy",
        "disappointed",
        "problem",
        "issue",
        "late",
        "delayed",
        "broken",
        "wrong",
        "complaint",
        "hate",
        "poor",
        "failed",
        "failure"
    ]

    text_lower = text.lower()

    positive_score = 0
    negative_score = 0

    for word in positive_words:
        if word in text_lower:
            positive_score += 1

    for word in negative_words:
        if word in text_lower:
            negative_score += 1

    if positive_score > negative_score:
        sentiment = "Positive"

    elif negative_score > positive_score:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "positive_score": positive_score,
        "negative_score": negative_score
    }