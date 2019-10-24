from django import forms

from .models import Room

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = (
            'name',
            'fields', 
            'numbers',
            'thief_x',
            'thief_y',
            'turn',
            'red_player',
            'red_villages_available',
            'red_villages_placed_x',
            'red_villages_placed_y',
            'red_cities_available',
            'red_cities_placed_x',
            'red_cities_placed_y',
            'red_roads_available',
            'red_roads_placed_x',
            'red_roads_placed_y',
            'green_player',
            'green_villages_available',
            'green_villages_placed_x',
            'green_villages_placed_y',
            'green_cities_available',
            'green_cities_placed_x',
            'green_cities_placed_y',
            'green_roads_available',
            'green_roads_placed_x',
            'green_roads_placed_y',
            'blue_player',
            'blue_villages_available',
            'blue_villages_placed_x',
            'blue_villages_placed_y',
            'blue_cities_available',
            'blue_cities_placed_x',
            'blue_cities_placed_y',
            'blue_roads_available',
            'blue_roads_placed_x',
            'blue_roads_placed_y',
            'white_player',
            'white_villages_available',
            'white_villages_placed_x',
            'white_villages_placed_y',
            'white_cities_available',
            'white_cities_placed_x',
            'white_cities_placed_y',
            'white_roads_available',
            'white_roads_placed_x',
            'white_roads_placed_y',


        ) 
