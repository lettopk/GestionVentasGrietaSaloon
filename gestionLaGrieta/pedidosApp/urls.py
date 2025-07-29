from django.urls import path
from . import views

app_name="pedido_mesa"

urlpatterns = [
    path('crear/', views.crear_pedido, name="crear"),
    path('agregar_pago/', views.agregar_metodo_pago, name="agregar_pago"),
    path('pago/<int:metodo_pago_id>/', views.agregar_metodo_pago, name="pago"),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="agregar"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="eliminar"),
    path('restar/<int:producto_id>/', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_pedido, name="limpiar"),
    path('', views.pedidos, name="Pedidos"),
    
]
