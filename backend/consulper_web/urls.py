from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1', include('djoser.urls')),
    path('api/v1', include('djoser.urls.authtoken')),
    # path('', include('services_app.urls')),
    # path('projects/', include('projects_app.urls')),
    # path('contact/', include('contact_app.urls')),
    path('api/v1/', include('services_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
