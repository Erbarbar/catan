# Generated by Django 2.2.4 on 2019-09-21 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_room_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='chat',
        ),
    ]
