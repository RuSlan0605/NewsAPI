from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from config.settings.base import MEDIA_ROOT, MEDIA_URL 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)