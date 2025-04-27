from .utils import get_sentiment
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def analyze_sentiment(request):
    if request.method == "POST":
        try:
            # Parse JSON body
            body = json.loads(request.body)
            text = body.get("text", "")

            # Validate text
            if not isinstance(text, str) or not text.strip():
                return JsonResponse({"error": "Invalid input. 'text' must be a non-empty string."}, status=400)

            # Get sentiment
            result = get_sentiment(text)
            return JsonResponse(result)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON body."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST requests are allowed."}, status=405)
