from django.contrib import admin
from .models import Service, Project

class ServiceAdmin(admin.ModelAdmin):
    search_fields=["service_name"]

class ProjectsAdmin(admin.ModelAdmin):
    search_fields=["title", "service_name"]
    list_filter=["service_name"]

admin.site.register(Service, ServiceAdmin)
admin.site.register(Project, ProjectsAdmin)
