from django.contrib import admin
from .models import metodo_pago,pedido,pedido_producto,metodo_pago_pedido

# Register your models here.
class pedido_Admin(admin.ModelAdmin):
    readonly_fields =('created', 'updated')
    
class metodo_pago_Admin(admin.ModelAdmin):
    readonly_fields =('created', 'updated')
    
admin.site.register(pedido,pedido_Admin)
admin.site.register(metodo_pago,metodo_pago_Admin)
admin.site.register(pedido_producto)
admin.site.register(metodo_pago_pedido)