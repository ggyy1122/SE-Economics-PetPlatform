# api/views.py
from django.http import JsonResponse

def your_view(request):
    return JsonResponse({"message": "Hello from API"})
