from django.views.generic.edit import CreateView
from .models import ImageFolder, Image
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ImageForm
from django.db.models import Q

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'home/login.html')
    else:
        folder = ImageFolder.objects.filter(user=request.user)
        image_results = Image.objects.all()
        query = request.GET.get("q")
        if query:
            folder = folder.filter(
                Q(imagefolder_title__icontains=query)

            ).distinct()
            image_results = image_results.filter(
                Q(image_title__icontains=query)
            ).distinct()
            return render(request, 'image/index.html', {
                'folder': folder,
                'image': image_results,
            })
        else:
            return render(request, 'image/index.html', {'folder': folder})


class ImageFolderCreate(CreateView):
    model = ImageFolder
    fields = ['folder_title', 'folder_logo']

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(ImageFolderCreate, self).form_valid(form)


class DetailView(generic.DetailView):
    model = ImageFolder
    template_name = 'image/detail.html'


def create_image(request, folder_id):
    form = ImageForm(request.POST or None, request.FILES or None)
    imagefolder = get_object_or_404(ImageFolder, pk=folder_id)
    if form.is_valid():
        folder_image = imagefolder.image_set.all()
        for s in folder_image:
            if s.image_title == form.cleaned_data.get("image_title"):
                context = {
                    'folder': imagefolder,
                    'form': form,
                    'error_message': 'You already added that image',
                }
                return render(request, 'image/create_image.html', context)
        image = form.save(commit=False)
        image.folder = imagefolder
        image.image_file = request.FILES['image_file']
        file_type = image.image_file.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_FILE_TYPES:
            context = {
                'folder': imagefolder,
                'form': form,
                'error_message': 'Image file must be png, jpg, jpeg'
            }
            return render(request, 'image/create_image.html', context)

        image.save()
        return render(request, 'image/detail.html', {'imagefolder': imagefolder})
    context = {
        'folder': imagefolder,
        'form': form,
    }
    return render(request, 'image/create_image.html', context)


def delete_folder(request, folder_id):
    print(folder_id)
    folder = ImageFolder.objects.get(pk=folder_id)
    folder.delete()
    folder = ImageFolder.objects.filter(user=request.user)
    return redirect('/image')


def delete_image(request, folder_id, image_id):
    imagefolder = get_object_or_404(ImageFolder, pk=folder_id)
    image = Image.objects.get(pk=image_id)
    image.delete()
    return render(request, 'image/detail.html', {'imagefolder': imagefolder})



