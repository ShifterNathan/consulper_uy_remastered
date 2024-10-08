# Generated by Django 5.1 on 2024-08-24 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('service_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, help_text='URL que tendrá la categoría', null=True, unique=True)),
                ('image', models.ImageField(upload_to='service_services')),
                ('description', models.CharField(help_text='Texto que aparecerá en la sección inicial', max_length=100)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
