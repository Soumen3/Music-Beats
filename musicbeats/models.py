from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    song_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=2000)
    singer=models.CharField(max_length=2000)
    tags= models.CharField(max_length=100)
    image= models.ImageField(upload_to="Documents/images")
    song= models.FileField(upload_to="Documents/songs")
    movie=models.CharField( max_length=100, default='unknown')
    credit=models.CharField( max_length=5000, null=True)

    def __str__(self):
        return self.name


class Favourite(models.Model):
    Favourite_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    song = models.ForeignKey(Song, on_delete=models.CASCADE, default='')
    
    
