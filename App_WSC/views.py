from django.shortcuts import render
from django.http import JsonResponse
import json

def index(request):
    return render(request, 'index.html')

def json_open(request):
    with open("Pet_feed.json",'r') as file:
        pet_feed_data = json.loads(file.read())
    return JsonResponse(pet_feed_data)