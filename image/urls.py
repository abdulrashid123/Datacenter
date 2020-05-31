from django.conf.urls import url, include
from . import views

app_name = 'image'


urlpatterns = [
    #/image/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^create_folder/$', views.ImageFolderCreate.as_view(), name='create_folder'),
    url(r'^(?P<folder_id>[0-9]+)/create_image/$', views.create_image, name='create_image'),
    url(r'^(?P<folder_id>[0-9]+)/delete_folder/$', views.delete_folder, name='delete_folder'),
    url(r'^(?P<folder_id>[0-9]+)/delete_image/(?P<image_id>[0-9]+)/$', views.delete_image, name='delete_image'),
    url(r'^$', include('video.urls')),


 ]