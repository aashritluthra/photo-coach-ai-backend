from django.urls import path, include

urlpatterns = [
    path('suggestions/', include('suggestions.urls')),
]
