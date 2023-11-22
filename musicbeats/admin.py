from django.contrib import admin
from .models import Song, Favourite
# Register your models here.
admin.site.register(Song)
admin.site.register(Favourite)