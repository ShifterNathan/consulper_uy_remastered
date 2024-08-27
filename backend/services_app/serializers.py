from rest_framework import serializers
from .models import Service, Project

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = (
            "service_name"
            "slug"
            "image"
            "description"
            "get_absolute_url"
            "get_image"
        )

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "service_name"
            "title"
            "slug"
            "description"
            "image"
            "thumbnail"
            "completedAt"
            "get_absolute_url"
            "get_image"
            "get_thumbnail"
        )