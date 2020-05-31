from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class DocumentFolder(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=1, on_delete=models.CASCADE)
    folder_title = models.CharField(blank=True, null=True, max_length=500)

    folder_logo = models.FileField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('document:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.folder_title


class Document(models.Model):
    folder = models.ForeignKey(DocumentFolder, on_delete=models.CASCADE)
    document_title = models.CharField(max_length=250)
    document_file = models.FileField(default='')

    def __str__(self):
        return self.document_title
