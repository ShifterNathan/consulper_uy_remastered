from django.contrib import admin
from .models import Service

class ServiceAdmin(admin.ModelAdmin):
    search_fields=["service_name"]


admin.site.register(Service, ServiceAdmin)
