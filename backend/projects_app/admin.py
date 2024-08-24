from django.contrib import admin
from .models import Project

class ProjectsAdmin(admin.ModelAdmin):
    search_fields=["title", "service_name"]
    list_filter=["service_name"]

admin.site.register(Project, ProjectsAdmin)