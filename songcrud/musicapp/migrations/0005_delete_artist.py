# Generated by Django 4.1.3 on 2022-11-12 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0004_remove_song_artist_id_delete_lyric_delete_song'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Artist',
        ),
    ]