from django.conf.urls import url, include
from . import views

urlpatterns = [
    #/Home/
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^$', views.logout_user, name='logout_user'),
    url(r'^welcome/$', views.welcome, name='welcome'),

]