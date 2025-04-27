from django.urls import path
from .views import get_sentiment

urlpatterns = [
    path('analyze/', get_sentiment, name='analyze_sentiment'),
]