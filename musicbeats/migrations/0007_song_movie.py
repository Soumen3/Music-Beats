# Generated by Django 4.2.7 on 2023-11-22 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0006_alter_song_image_alter_song_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='movie',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
