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
            'green_player',
            'blue_player',
            'white_player'
        ) 
