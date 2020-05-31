from django.conf.urls import url, include
from . import views

app_name = 'table'


urlpatterns = [
    #/table/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^create_table/$', views.TableCreate.as_view(), name='create_table'),
    url(r'^code/$', views.code, name='code'),
    url(r'^(?P<table_id>[0-9]+)/create_parameter/$', views.create_parameter, name='create_parameter'),
    #url(r'^(?P<table_id>[0-9]+)/create_parameter/$', views.ParameterCreate.as_view(), name='create_parameter'),
    url(r'^(?P<table_id>[0-9]+)/delete_table/$', views.delete_table, name='delete_table'),
    url(r'^$', include('video.urls')),


 ]
