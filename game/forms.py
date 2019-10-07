from django import forms

from .models import Room

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = (
            'name',
            'fields', 
            'numbers',

            'red_player',
            'red_villages_placed_x',
            'red_villages_placed_y',
            'green_player',
            'green_villages_placed_x',
            'green_villages_placed_y',
            'blue_player',
            'blue_villages_placed_x',
            'blue_villages_placed_y',
            'white_player',
            'white_villages_placed_x',
            'white_villages_placed_y',


        ) 
