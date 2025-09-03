from django.db import models
from inventarioApp.models import producto

# Create your models here.
class Gasto(models.Model):
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()
    precio_total = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)