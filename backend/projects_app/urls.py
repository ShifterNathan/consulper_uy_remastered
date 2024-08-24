from django.urls import path
from projects_app import views

urlpatterns = [

    path('', views.project_list, name='Project'),
    path('<slug:service_slug>', views.project_list, name='project'),

]
