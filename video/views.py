from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .forms import  VideoForm
from Home.form import UserForm
from django.views import generic
from django.db.models import Q
from .models import Folder, Video
from django.views.generic.edit import CreateView

from django.contrib.auth.models import User

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']
VIDEO_FILE_TYPES = ['ts', 'mp4', 'mkv']


class DetailView(generic.DetailView):
    model = Folder
    template_name = 'video/detail.html'


class FolderCreate(CreateView):
    model = Folder
    fields = ['folder_title', 'folder_logo']

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(FolderCreate, self).form_valid(form)

def delete_folder(request, folder_id):
    folder = Folder.objects.get(pk=folder_id)
    folder.delete()
    folder = Folder.objects.filter(user=request.user)
    return redirect('/video')


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'home/login.html')
    else:
        folder = Folder.objects.filter(user=request.user)
        video_results = Video.objects.all()
        query = request.GET.get("q")
        if query:
            folder = folder.filter(
                Q(folder_title__icontains=query)

            ).distinct()
            video_results = video_results.filter(
                Q(video_title__icontains=query)
            ).distinct()
            return render(request, 'video/index.html', {
                'folder': folder,
                'video': video_results,
            })
        else:
            return render(request, 'video/index.html', {'folder': folder})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return redirect('/home')


def create_video(request, folder_id):
    form = VideoForm(request.POST or None, request.FILES or None)
    folder = get_object_or_404(Folder, pk=folder_id)
    if form.is_valid():
        folder_video = folder.video_set.all()
        for s in folder_video:
            if s.video_title == form.cleaned_data.get("video_title"):
                context = {
                    'folder': folder,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'video/create_video.html', context)
        video = form.save(commit=False)
        video.folder = folder
        video.video_file = request.FILES['video_file']
        file_type = video.video_file.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in VIDEO_FILE_TYPES:
            context = {
                'folder': folder,
                'form': form,
                'error_message': 'Video file must be TS, MP4, or MKV',
            }
            return render(request, 'video/create_video.html', context)

        video.save()
        return render(request, 'video/detail.html', {'folder': folder})
    context = {
        'folder': folder,
        'form': form,
    }
    return render(request, 'video/create_video.html', context)


def delete_video(request, folder_id, video_id):
    folder = get_object_or_404(Folder, pk=folder_id)
    video = Video.objects.get(pk=video_id)
    video.delete()
    return render(request, 'video/detail.html', {'folder': folder})


def home_return(request):
    return render(request, 'home/welcome.html')



