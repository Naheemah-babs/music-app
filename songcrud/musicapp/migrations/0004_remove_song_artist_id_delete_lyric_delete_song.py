# Generated by Django 4.1.3 on 2022-11-12 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_lyric_content_lyric_song_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artist_id',
        ),
        migrations.DeleteModel(
            name='Lyric',
        ),
        migrations.DeleteModel(
            name='Song',
        ),
    ]