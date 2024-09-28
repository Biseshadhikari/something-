# event_app/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Ensure you have this template
def contact(request):
    return render(request, 'contact.html')  # Ensure you have this template