import os
import json
import google.generativeai as genai
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Configure the Gemini API
genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

@method_decorator(csrf_exempt, name='dispatch')
class SuggestionsView(View):
    def get(self, request):
        return render(request, 'suggestions/index.html')

    def post(self, request):
        try:
            # Parse the JSON request body
            data = json.loads(request.body)
            text = data.get('text')
            
            if not text:
                return JsonResponse(
                    {"error": "No text provided"}, 
                    status=400
                )
            
            # Create a prompt that requests a structured, concise response
            prompt = f"""Given this text: "{text}"
            Provide a structured response in exactly 6 words or less.
            Format: "Category: Response"
            Example: "Style: Minimalist and clean"
            """
            
            # Generate response using Gemini
            response = model.generate_content(prompt)
            
            return JsonResponse({
                "suggestion": response.text
            })
            
        except json.JSONDecodeError:
            return JsonResponse(
                {"error": "Invalid JSON"}, 
                status=400
            )
        except Exception as e:
            print(f"Error details: {str(e)}")
            return JsonResponse(
                {"error": str(e)}, 
                status=500
            )