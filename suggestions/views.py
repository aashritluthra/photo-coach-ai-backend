import os
from django.http import JsonResponse
from django.views import View
from django.conf import settings

class SuggestionsView(View):
    def post(self, request):
        return JsonResponse({"message": "POST request received!"})