from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ImageFolder(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=1, on_delete=models.CASCADE)
    folder_title = models.CharField(blank=True, null=True, max_length=500)

    folder_logo = models.FileField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('image:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.folder_title


class Image(models.Model):
    folder = models.ForeignKey(ImageFolder, on_delete=models.CASCADE)
    image_title = models.CharField(max_length=250)
    image_file = models.FileField(default='')

    def __str__(self):
        return self.image_title
