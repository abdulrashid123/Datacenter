from .models import DocumentFolder,Document
from django.views.generic.edit import CreateView
from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DocumentForm
from django.db.models import Q

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'home/login.html')
    else:
        folder = DocumentFolder.objects.filter(user=request.user)
        image_results = Document.objects.all()
        query = request.GET.get("q")
        if query:
            folder = folder.filter(
                Q(folder_title__icontains=query)

            ).distinct()
            document_results = image_results.filter(
                Q(document_title__icontains=query)
            ).distinct()
            return render(request, 'document/index.html', {
                'folder': folder,
                'document': document_results,
            })
        else:
            return render(request, 'document/index.html', {'folder': folder})


class DocumentFolderCreate(CreateView):
    model = DocumentFolder
    fields = ['folder_title', 'folder_logo']

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(DocumentFolderCreate, self).form_valid(form)


class DetailView(generic.DetailView):
    model = DocumentFolder
    template_name = 'document/detail.html'


def create_document(request, folder_id):
    form = DocumentForm(request.POST or None, request.FILES or None)
    documentfolder = get_object_or_404(DocumentFolder, pk=folder_id)
    if form.is_valid():
        folder_doc = documentfolder.document_set.all()
        for s in folder_doc:
            if s.document_title == form.cleaned_data.get("document_title"):
                context = {
                    'folder': documentfolder,
                    'form': form,
                    'error_message': 'You already added that document',
                }
                return render(request, 'document/create_document.html', context)
        document = form.save(commit=False)
        document.folder = documentfolder
        document.document_file = request.FILES['document_file']
        document.save()
        return render(request, 'document/detail.html', {'documentfolder': documentfolder})
    context = {
        'folder': documentfolder,
        'form': form,
    }
    return render(request, 'document/create_document.html', context)


def delete_folder(request, folder_id):
    folder = DocumentFolder.objects.get(pk=folder_id)
    folder.delete()
    folder = DocumentFolder.objects.filter(user=request.user)
    return redirect('/document')


def delete_document(request, folder_id, document_id):
    documentfolder = get_object_or_404(DocumentFolder, pk=folder_id)
    document = Document.objects.get(pk=document_id)
    document.delete()
    return render(request, 'document/detail.html', {'documentfolder': documentfolder})



