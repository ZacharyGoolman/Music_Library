# Generated by Django 4.0.4 on 2022-04-26 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0003_song_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='media',
            field=models.CharField(default='no image', max_length=250),
        ),
    ]
