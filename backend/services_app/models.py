from django.db import models
from django.urls import  reverse
from django.utils.text import slugify

class Service(models.Model):
    service_name=models.CharField(primary_key=True, max_length=50)
    slug=models.SlugField(unique=True, blank=True, null=True, help_text="URL que tendrá la categoría")
    image=models.ImageField(upload_to='service_services')
    description=models.CharField(max_length=100, help_text="Texto que aparecerá en la sección inicial")

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)   

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services_by_category', args=[self.slug])
