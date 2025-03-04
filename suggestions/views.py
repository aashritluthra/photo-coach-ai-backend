from django.http import JsonResponse
from django.views import View

class SuggestionsView(View):
    def get(self, request):
        return JsonResponse({"message": "GET request received!"})