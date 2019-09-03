from django.db import models

# Create your models here.
class Room(models.Model):

    name = models.SlugField(max_length=100, unique=True)

    fields = models.CharField(max_length=37)
    numbers = models.CharField(max_length=40)

    villagesX = models.CharField(max_length=1000, null=True, blank=True)
    villagesY = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return "%s" % (self.name)