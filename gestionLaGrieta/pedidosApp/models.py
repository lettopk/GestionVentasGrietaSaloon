from django.db import models
from django.contrib.auth.models import User
from inventarioApp.models import producto
# Create your models here.

    #Modelo-Tabla Metodo de pago 
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
    created = models.DateTimeField(auto_now_add= True)
    updated = models.DateTimeField(auto_now_add= True)
    vendedor =  models.ForeignKey(User, on_delete=models.CASCADE)    #Relacionado a los pedidos (uno a muchos), si se elimina el vendedor, se eliminan todos los pedidos

    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
    
    def __str__(self):
        return self.mesa
    
class pedido_producto(models.Model):
    pedido = models.ForeignKey(pedido, on_delete=models.CASCADE, related_name="productos")
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.PositiveIntegerField()
    
    def subtotal(self):
        return self.cantidad * self.precio_unitario
        
    def __str__(self):
        return f"{self.producto.titulo} x {self.cantidad}"
    
class metodo_pago_pedido(models.Model):
    pedido = models.ForeignKey(pedido, on_delete=models.CASCADE, related_name="metodo_pago_pedido")
    metodo_pago = models.ForeignKey(metodo_pago, on_delete=models.CASCADE)
    valor = models.PositiveIntegerField()
    