from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('contact/', include('contact.urls')),
    path('employee/', include('employee.urls')),
    path('serv/', include('serv.urls')),
    path('portfo/', include('portfo.urls')),
    path('clients/', include('clients.urls')),
    path('authentication/', include('authentication.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)