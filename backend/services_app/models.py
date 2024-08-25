from django.db import models
from django.urls import  reverse
from django.core.files import File
from django.utils.text import slugify

from io import BytesIO
from PIL import Image

class Service(models.Model):
    service_name=models.CharField(primary_key=True, max_length=50)
    slug=models.SlugField(unique=True, blank=True, null=True, help_text="URL que tendrá la categoría")
    image=models.ImageField(upload_to='service_services')
    description=models.CharField(max_length=100, help_text="Texto que aparecerá en la sección inicial")

    class Meta:
        ordering = ('service_name')
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)   

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}'
        # return reverse('projects_by_services', args=[self.slug])
    
    def get_image(self):
        if self.image:
            return 'https://127.0.0.1:8000' + self.image.url
        return ''

class Project(models.Model):
    service_name=models.ForeignKey(Service, related_name='project', null=True, on_delete=models.SET_NULL)
    title=models.CharField(max_length=50, null=False)
    slug=models.SlugField(unique=True, blank=True, null=True, help_text="URL que tendrá la categoría")
    description=models.CharField(max_length=255, null=True, blank=True, help_text="Descripción de la obra")
    image=models.ImageField(upload_to='project_projects')
    thumbnail=models.ImageField(upload_to='project_projects')
    completedAt=models.DateField(help_text="Fecha en la que se completo la obra")

    class Meta:
        ordering = ('title')
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
    
    def __str__(self):
        return '%s de %s' % (self.service_name, self.title) 
    
    def get_absolute_url(self):
        return f'/{self.service_name.slug}/{self.slug}'
    
    def get_image(self):
        if self.image:
            return 'https://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.image:
            return 'https://127.0.0.1:8000' + self.image.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return 'https://127.0.0.1:8000' + self.thumbnail.url
            else: 
                return ''
            
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality = 85)
        thumbnail = File(thumb_io, name=image.name)

        return thumbnail