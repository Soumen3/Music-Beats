# Generated by Django 4.2.7 on 2023-11-22 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0009_song_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='credit',
            field=models.CharField(default='', max_length=5000, null=True),
        ),
    ]
