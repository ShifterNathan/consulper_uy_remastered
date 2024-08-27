from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from services_app import views

urlpatterns = [
    path('services/', views.ServicesList.as_view()),
    path('projects/', views.ProjectsList.as_view()),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)