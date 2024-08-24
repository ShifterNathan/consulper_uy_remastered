from django.shortcuts import render, get_object_or_404
from .models import Project
from services_app.models import Service

'''    def projects(request):
        projects = projects.objects.all()
        services = Service.objects.all()
        return render(request, "projects_app/projects.html", {"projects": projects, "services": services})
'''

def project_list(request,service_slug=None):
    service = None
    services = Service.objects.all()
    projects = Project.objects.all()
    if service_slug:
        service = get_object_or_404(Service,slug=service_slug)
        projects = projects.filter(service=service)
    return render(request, 'projects_app/projects.html', {'services':services, 'service':service, 'projects':projects,})
