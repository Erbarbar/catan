from django import forms

from .models import Room

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = (
            'name',
            'fields', 
            'numbers',
            'villagesX', 
            'villagesY',

            'red_player',
            'red_villages_placed_x',
            'red_villages_placed_y',
            'green_player',
            'blue_player',
            'white_player'


        ) 
