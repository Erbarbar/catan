# game/views.py
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe
from django.template.defaultfilters import slugify
from .models import Room
from .forms import RoomForm
import json
import random

def index(request):
    return render(request, 'game/index.html', {})

def room(request, room_name):
    room_name = slugify(room_name)
    if not Room.objects.filter(name=room_name).exists():
        createRoom(room_name)

    room = get_object_or_404(Room, name=room_name)
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            room.name = form.cleaned_data['name']
            room.fields = form.cleaned_data['fields']
            room.numbers = form.cleaned_data['numbers']
            room.villagesX = form.cleaned_data['villagesX']
            room.villagesY = form.cleaned_data['villagesY']
            room.save()
            form.save()

    else:
        form = RoomForm(instance=room)
    return render(request, 'game/room.html', {
        'room': room,
        'form': form
        })




def createRoom(room_name):
    fields = ["l", "l", "l", "l", "b", "b", "b", "g", "g", "g", "g", "w", "w", "w", "w", "o", "o", "o", "d"]
    numbers = ["2", "3", "3", "4", "4", "5", "5", "6", "6", "8", "8", "9", "9", "10", "10", "11", "11", "12"]
    random.shuffle(fields)
    random.shuffle(numbers)
    fields = ','.join(fields)
    numbers = ','.join(numbers)
    newRoom = Room(name=room_name, fields=fields, numbers=numbers)
    newRoom.save()

    