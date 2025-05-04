from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .utils import analyze_single_text, analyze_decision

@csrf_exempt
def get_sentiment(request):
    """
    Django view to handle a batch of texts and return sentiments and a decision summary.
    """
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            texts = body.get("texts", [])

            if not texts or not isinstance(texts, list):
                return JsonResponse({"error": "'texts' must be a non-empty list of strings."}, status=400)

            results = []
            for text in texts:
                if not isinstance(text, str) or not text.strip():
                    results.append({
                        "text": text,
                        "error": "Invalid or empty text"
                    })
                    continue

                result = analyze_single_text(text)
                result["text"] = text
                results.append(result)

            decision_summary = analyze_decision(results)

            return JsonResponse({
                "results": results,
                "summary": decision_summary
            })

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "POST method required"}, status=405)
