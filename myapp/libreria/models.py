from django.db import models
from django.forms import ImageField

# Create your models here.
class Libro(models.Model):
    
    titulo = models.CharField(max_length=100, verbose_name='titulo')
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='imagen', null=True)
    descripcion = models.CharField(max_length=500 ,verbose_name='descripcion', null=True)

    def __str__(self):
        return self.titulo
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()