from textblob import TextBlob

def analyze_sentiment(text):
    """Analyze the sentiment of a given text using TextBlob.

    Args:
        text (str): The text to analyze.

    Returns:
        str: The sentiment polarity of the text.
    """
    blob = TextBlob(text)
    polarity= blob.sentiment.polarity

    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    else:
        return "Neutral"