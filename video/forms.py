from django import forms
from django.contrib.auth.models import User

from .models import Folder, Video


class FolderForm(forms.ModelForm):

    class Meta:
        model = Folder
        fields = ['folder_title', 'folder_logo']


class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['video_title', 'video_file']


