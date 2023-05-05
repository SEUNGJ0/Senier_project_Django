from django.shortcuts import render
from django.http import JsonResponse
import json

def index(request):
    return render(request, 'index.html')

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })

def json_open(request):
    with open("Pet_feed.json",'r') as file:
        pet_feed_data = json.loads(file.read())
    return JsonResponse(pet_feed_data)