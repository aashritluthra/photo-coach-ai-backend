import os
import json
import google.generativeai as genai
from django.http import JsonResponse
from django.views import View
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from PIL import Image
import io


# exempt this view from csrf protection
@method_decorator(csrf_exempt, name='dispatch')
class SuggestionsView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def get(self, request):
        return render(request, 'suggestions/index.html')

    # handle the post request, currently only handles image processing, no text processing
    def post(self, request):
        try:            
            image_file = request.FILES.get('image') 
            if not image_file: return JsonResponse({"error": "No image provided"}, status=400)
            
            # Convert the image to PIL Image
            image = Image.open(image_file)
            
            # Create a prompt that requests a structured, concise response, need to tweak this 
            prompt = """ This is a snapshot of a photograph I am taking. Give me actionable photography 
            suggestions with a focus on composition, lighting, or style aspects in a concise response. This 
            suggestion will be used to help me improve my photography skills and will show on the user's 
            screen while taking the photograph. The suggestion should be concise with a maximum of 6 words.
            The suggestion should focus on what the user can tweak about the picture. I.e. ISO, white balance, 
            composure, focus, aperture, shutter speed. The suggestion should be simple and something an amateur
            photographer or smart phone user can understand. Tell the user exactly which setting to change. 
            Dont tell me anything apart from the suggestion. 
            Format: "Actionable Suggestion while taking the photograph"
            Example: "Move closer to the subject".
            Example 2: "Lower the white balance a bit"""
            
            # Generate response using Gemini Vision
            response = self.model.generate_content([prompt, image])
            
            return JsonResponse({
                "suggestion": response.text
            })
            
        except Exception as e:
            print(f"Error details: {str(e)}")
            return JsonResponse(
                {"error": str(e)}, 
                status=500
            )
