# Generated by Django 4.2.7 on 2023-11-22 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musicbeats', '0011_watchlater'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlater',
            name='song',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='musicbeats.song'),
        ),
        migrations.AddField(
            model_name='watchlater',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
