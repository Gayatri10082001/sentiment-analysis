from django.views.decorators.csrf import csrf_exempt
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.nn.functional import softmax
import torch
from django.http import JsonResponse
import json

# Load once at the top
tokenizer = AutoTokenizer.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")
model = AutoModelForSequenceClassification.from_pretrained("nlptown/bert-base-multilingual-uncased-sentiment")

@csrf_exempt
def get_sentiment(request):
    """
    Django view to analyze the sentiment of the given text and return the sentiment, confidence, and star rating.
    """
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            text = body.get('text', '')
            
            if not text:
                return JsonResponse({"error": "No text provided"}, status=400)

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

            result = {
                "sentiment": sentiment,
                "confidence": round(confidence, 2),
                "stars": star_rating
            }
            return JsonResponse(result)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    else:
        return JsonResponse({"error": "POST method required"}, status=405)
