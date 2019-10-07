# game/views.py
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils.safestring import mark_safe
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Room
from .forms import RoomForm
import json
import random




def index(request):
    return render(request, 'game/index.html', {})

@login_required
def room(request, room_name):
    room_name = slugify(room_name)

    if not Room.objects.filter(name=room_name).exists():
        createRoom(room_name)

    room = get_object_or_404(Room, name=room_name)
    form = RoomForm()
    if request.method == "POST":
        print(request.POST)

        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            room.name = form.cleaned_data['name']
            room.fields = form.cleaned_data['fields']
            room.numbers = form.cleaned_data['numbers']
            room.red_villages_placed_x = form.cleaned_data['red_villages_placed_x']
            room.red_villages_placed_y = form.cleaned_data['red_villages_placed_y']
            room.green_villages_placed_x = form.cleaned_data['green_villages_placed_x']
            room.green_villages_placed_y = form.cleaned_data['green_villages_placed_y']
            room.blue_villages_placed_x = form.cleaned_data['blue_villages_placed_x']
            room.blue_villages_placed_y = form.cleaned_data['blue_villages_placed_y']
            room.white_villages_placed_x = form.cleaned_data['white_villages_placed_x']
            room.white_villages_placed_y = form.cleaned_data['white_villages_placed_y']
            room.save()
            form.save()
    else:
        form = RoomForm(instance=room)

    return render(request, 'game/room.html', {
        'room': room,
        'form': form,
        'user': request.user
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

def createHand(color):
    pass