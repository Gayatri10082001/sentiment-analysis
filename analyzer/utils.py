import torch
from torch.nn.functional import softmax
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax
import torch
from django.http import JsonResponse
import json

# Load once at the top
tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_single_text(text):
    """
    Analyze sentiment for a single text input.
    Returns a dict with sentiment, confidence, and star rating.
    """
    inputs = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = softmax(outputs.logits, dim=1)
    confidence, predicted_class = torch.max(probs, dim=1)
    confidence = confidence.item()
    star_rating = predicted_class.item() + 1

    if star_rating <= 2:
        sentiment = "Negative"
    elif star_rating == 3:
        sentiment = "Neutral"
    else:
        sentiment = "Positive"

    return {
        "sentiment": sentiment,
        "confidence": round(confidence, 2),
        "stars": star_rating
    }

def analyze_decision(results):
    """
    Analyze a list of sentiment results and return a decision with reasoning.
    """
    total = len(results)
    sentiment_counts = {"Positive": 0, "Neutral": 0, "Negative": 0}
    star_sum = 0

    for item in results:
        if "stars" not in item:
            continue
        sentiment = item.get("sentiment")
        stars = item.get("stars", 0)

        if sentiment in sentiment_counts:
            sentiment_counts[sentiment] += 1
        star_sum += stars

    valid_count = sum(sentiment_counts.values())
    avg_stars = star_sum / valid_count if valid_count else 0

    if sentiment_counts["Negative"] >= valid_count / 2:
        decision = "Do not proceed."
        reason = "The majority of feedback is negative."
    elif avg_stars >= 4.0:
        decision = "Proceed with confidence."
        reason = f"Feedback is mostly positive with an average rating of {avg_stars:.1f}."
    elif avg_stars >= 3.0:
        decision = "Proceed with caution."
        reason = f"Mixed feedback with an average rating of {avg_stars:.1f}."
    else:
        decision = "Hold off."
        reason = "Low average rating and mixed sentiment."

    return {
        "decision": decision,
        "reason": reason,
        "summary": {
            "positive": sentiment_counts["Positive"],
            "neutral": sentiment_counts["Neutral"],
            "negative": sentiment_counts["Negative"],
            "average_stars": round(avg_stars, 2)
        }
    }
