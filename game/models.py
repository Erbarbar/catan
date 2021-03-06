from django.db import models
from django.conf import settings

# Create your models here.
class Room(models.Model):

    name = models.SlugField(max_length=100, unique=True)

    fields = models.CharField(max_length=37)
    numbers = models.CharField(max_length=40)

    thief_x = models.IntegerField(default=0);
    thief_y = models.IntegerField(default=0);

    turn = models.CharField(max_length=10, default="none");

    red_player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="red_player", null=True, blank=True)
    red_villages_placed_x = models.CharField(max_length=1000, null= True, blank=True, default="")
    red_villages_placed_y = models.CharField(max_length=1000, null= True, blank=True, default="")
    red_villages_available = models.IntegerField(default=5)
    red_cities_placed_x = models.CharField(max_length=1000, null= True, blank=True, default="")
    red_cities_placed_y = models.CharField(max_length=1000, null= True, blank=True, default="")
    red_cities_available = models.IntegerField(default=4)
    red_roads_placed_x = models.CharField(max_length=1000, null= True, blank=True, default="")
    red_roads_placed_y = models.CharField(max_length=1000, null= True, blank=True, default="")
    red_roads_available = models.IntegerField(default=15)
    red_wheat = models.IntegerField(default=0)
    red_brick = models.IntegerField(default=0)
    red_wool = models.IntegerField(default=0)
    red_stone = models.IntegerField(default=0)

    green_player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="green_player", null=True, blank=True)
    green_villages_placed_x = models.CharField(max_length=1000, null= True, blank=True, default="")
    green_villages_placed_y = models.CharField(max_length=1000, null= True, blank=True, default="")
    green_villages_available = models.IntegerField(default=5)
    green_cities_placed_x = models.CharField(max_length=1000, null= True, blank=True, default="")
    green_cities_placed_y = models.CharField(max_length=1000, null= True, blank=True, default="")
    green_cities_available = models.IntegerField(default=4)
    green_roads_placed_x = models.CharField(max_length=1000, null= True, blank=True, default="")
    green_roads_placed_y = models.CharField(max_length=1000, null= True, blank=True, default="")
    green_roads_available = models.IntegerField(default=15)
    green_wheat = models.IntegerField(default=0)
    green_brick = models.IntegerField(default=0)
    green_wool = models.IntegerField(default=0)
    green_stone = models.IntegerField(default=0)

    blue_player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="blue_player", null=True, blank=True)
    blue_villages_placed_x = models.CharField(max_length=1000, null= True, blank=True, default="")
    blue_villages_placed_y = models.CharField(max_length=1000, null= True, blank=True, default="")
    blue_villages_available = models.IntegerField(default=5)
    blue_cities_placed_x = models.CharField(max_length=1000, null= True, blank=True, default="")
    blue_cities_placed_y = models.CharField(max_length=1000, null= True, blank=True, default="")
    blue_cities_available = models.IntegerField(default=4)
    blue_roads_placed_x = models.CharField(max_length=1000, null= True, blank=True, default="")
    blue_roads_placed_y = models.CharField(max_length=1000, null= True, blank=True, default="")
    blue_roads_available = models.IntegerField(default=15)
    blue_wheat = models.IntegerField(default=0)
    blue_brick = models.IntegerField(default=0)
    blue_wool = models.IntegerField(default=0)
    blue_stone = models.IntegerField(default=0)

    white_player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, related_name="white_player", null=True, blank=True)
    white_villages_placed_x = models.CharField(max_length=1000, null= True, blank=True, default="")
    white_villages_placed_y = models.CharField(max_length=1000, null= True, blank=True, default="")
    white_villages_available = models.IntegerField(default=5)
    white_cities_placed_x = models.CharField(max_length=1000, null= True, blank=True, default="")
    white_cities_placed_y = models.CharField(max_length=1000, null= True, blank=True, default="")
    white_cities_available = models.IntegerField(default=4)
    white_roads_placed_x = models.CharField(max_length=1000, null= True, blank=True, default="")
    white_roads_placed_y = models.CharField(max_length=1000, null= True, blank=True, default="")
    white_roads_available = models.IntegerField(default=15)
    white_wheat = models.IntegerField(default=0)
    white_brick = models.IntegerField(default=0)
    white_wool = models.IntegerField(default=0)
    white_stone = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % (self.name)
