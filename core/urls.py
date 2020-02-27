from django.conf.urls import url
from django.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^org/', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^files/', include('db_file_storage.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'app.views.handler404'
