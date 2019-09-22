# Generated by Django 2.2.4 on 2019-09-21 22:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0006_remove_room_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerHand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, choices=[('r', 'red'), ('g', 'green'), ('b', 'blue'), ('w', 'white')], max_length=5, null=True)),
                ('wheat', models.IntegerField(default=0)),
                ('brick', models.IntegerField(default=0)),
                ('wool', models.IntegerField(default=0)),
                ('stone', models.IntegerField(default=0)),
                ('villages', models.IntegerField(default=5)),
                ('cities', models.IntegerField(default=4)),
                ('roads', models.IntegerField(default=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]