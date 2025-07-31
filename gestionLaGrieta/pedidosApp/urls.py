from django.urls import path
from . import views

app_name="pedido_mesa"

urlpatterns = [
    path('crear/', views.crear_pedido, name="crear"),
    path('agregar_pago/', views.agregar_metodo_pago, name="agregar_pago"),
    path('agregar_producto/', views.agregar_producto, name="agregar_producto"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="eliminar"),
    path('restar/<int:producto_id>/', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_pedido, name="limpiar"),
    path('', views.pedidos, name="Pedidos"),
    
]
