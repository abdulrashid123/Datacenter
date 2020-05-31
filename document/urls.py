from django.conf.urls import url
from . import views

app_name = 'document'


urlpatterns = [
    #/document/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^create_folder/$', views.DocumentFolderCreate.as_view(), name='create_folder'),
    url(r'^(?P<folder_id>[0-9]+)/create_document/$', views.create_document, name='create_document'),
    url(r'^(?P<folder_id>[0-9]+)/delete_folder/$', views.delete_folder, name='delete_folder'),
    url(r'^(?P<folder_id>[0-9]+)/delete_document/(?P<document_id>[0-9]+)/$', views.delete_document, name='delete_document'),
]