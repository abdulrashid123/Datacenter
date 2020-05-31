from django.conf.urls import url
from . import views


app_name = 'video'


urlpatterns = [
    #/video/
    url(r'^$', views.index, name='index'),
    url(r'^create_folder/$', views.FolderCreate.as_view(), name='create_folder'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<folder_id>[0-9]+)/delete_folder/$', views.delete_folder, name='delete_folder'),
    url(r'^(?P<folder_id>[0-9]+)/create_video/$', views.create_video, name='create_video'),
    url(r'^(?P<folder_id>[0-9]+)/delete_video/(?P<video_id>[0-9]+)/$', views.delete_video, name='delete_video'),
    url(r'^back/$', views.home_return, name='home_return'),

 ]