from django.db import models
from django.utils import timezone
# Create your models here.
# modelo para cada producto dentro del inventerio

class producto (models.Model ):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to= 'productos', null=True, blank=True)  #subcarpeta paraguardar imagenes, pla carga deimagenes es opcional
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()
    precio_total = models.IntegerField()
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now_add= True)
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
    
    def __str__(self):
        return self.titulo