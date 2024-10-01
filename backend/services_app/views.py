from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Service, Project
from .serializers import ServiceSerializer, ProjectSerializer

class ServicesList(APIView):
    def get(self, request, format=None):
        services = Service.objects.all()[0:4]
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

class ProjectsList(APIView): 
    def get(self, request, format=None):
        projects = Project.objects.all()[0:10]
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class ProjectDetail(APIView):
    def get_object(self, service_slug, project_slug):
        project = self.get_object(service_slug, project_slug)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)


# def home(request):
#     services = Service.objects.all()
#     return render(request, "home_app/home.html", {"services": services})
