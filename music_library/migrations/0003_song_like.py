# Generated by Django 4.0.4 on 2022-04-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0002_song_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
