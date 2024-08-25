from django.db import models
from django.core.files import File
from services_app.models import Service

from io import BytesIO
from PIL import Image

class Project(models.Model):
    service_name=models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=50, null=False)
    slug=models.SlugField(unique=True, blank=True, null=True, help_text="URL que tendrá la categoría")
    description=models.CharField(max_length=255, null=True, blank=True, help_text="Descripción de la obra")
    image=models.ImageField(upload_to='project_projects')
    completedAt=models.DateField(help_text="Fecha en la que se completo la obra")

    class Meta:
        ordering = ('title')
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
    
    def __str__(self):
        return '%s de %s' % (self.service_name, self.title) 
    
    def get_absolute_url(self):
        return f'/{self.slug}'

