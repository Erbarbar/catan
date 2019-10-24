# Generated by Django 2.2.4 on 2019-10-24 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_auto_20191018_1635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='blue_cities',
            new_name='blue_cities_available',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='blue_roads',
            new_name='blue_roads_available',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='blue_villages',
            new_name='blue_villages_available',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='green_cities',
            new_name='green_cities_available',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='green_roads',
            new_name='green_roads_available',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='green_villages',
            new_name='green_villages_available',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='red_cities',
            new_name='red_cities_available',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='red_roads',
            new_name='red_roads_available',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='red_villages',
            new_name='red_villages_available',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='white_cities',
            new_name='white_cities_available',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='white_roads',
            new_name='white_roads_available',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='white_villages',
            new_name='white_villages_available',
        ),
    ]
