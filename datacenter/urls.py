
from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include(('Home.urls','home'), namespace='home')),
    url(r'^music/', include('music.urls')),
    url(r'^video/', include('video.urls')),
    url(r'^image/', include('image.urls')),
    url(r'^table/', include('table.urls')),
    url(r'^document/', include(('document.urls', 'document'), namespace='document')),
]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
