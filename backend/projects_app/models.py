from django.db import models
from services_app.models import Service

class Project(models.Model):
    service_name=models.ForeignKey(Service, null=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=50, null=False)
    slug=models.SlugField(unique=True, blank=True, null=True, help_text="URL que tendrá la categoría")
    description=models.CharField(max_length=255, null=True, blank=True, help_text="Descripción de la obra")
    image=models.ImageField(upload_to='project_projects')
    completedAt=models.DateField(help_text="Fecha en la que se completo la obra")

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
    
    def __str__(self):
        return '%s de %s' % (self.category, self.title)
