from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import analyze_sentiment

# Create your views here.

@csrf_exempt
def analyze(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text', '')
            sentiment = analyze_sentiment(text)
            return JsonResponse({'sentiment': sentiment})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
