from django.db import models
from django.contrib.auth.models import User
from inventarioApp.models import producto
# Create your models here.

    #Modelo-Tabla Mtodo de pago 
class metodo_pago(models.Model):
    titulo = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to= 'metodo_pago')  #subcarpeta para guardar imagenes
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now_add= True)
    class Meta:
        verbose_name = 'metodo_pago'
        verbose_name_plural = 'metodos_pago'
        
    def __str__(self):
        return self.titulo
    
    #Modelo-Tabla pedido
class pedido(models.Model):
    mesa = models.CharField(max_length=30)
    producto = models.ManyToManyField(producto)                     #Relacionado a los productos (muchos a muchos)
    metodos_pago = models.ManyToManyField(metodo_pago)
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now_add= True)
    vendedor =  models.ForeignKey(User, on_delete=models.CASCADE)    #Relacionado a los pedidos (uno a muchos), si se elimina el vendedor, se eliminan todos los pedidos
    metodos_pago = models.ManyToManyField(metodo_pago)
    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
    
    def __str__(self):
        return self.mesa