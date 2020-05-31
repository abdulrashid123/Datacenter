from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Album(models.Model):
    user = models.ForeignKey(User, null= True,   on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + '_' + self.artist

    @property
    def album_logo_url(self):
        if self.album_logo and hasattr(self.album_logo, 'url'):
            return self.album_logo.url



class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    audio_file = models.FileField(default='')
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default= False)

    def __str__(self):
        return self.song_title

    @property
    def audio_file_url(self):
        if self.audio_file and hasattr(self.audio_file, 'url'):
            return self.audio_file.url
