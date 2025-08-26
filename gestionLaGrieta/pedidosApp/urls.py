from django.urls import path
from . import views

app_name="pedido_mesa"

urlpatterns = [
    path('', views.pedidos, name="Pedidos"),
    path('crear/', views.crear_pedido, name="crear"),
    path('agregar_pago/', views.agregar_metodo_pago, name="agregar_pago"),
    path('agregar_producto/', views.agregar_producto, name="agregar_producto"),
    path('incrementar_cantidad/<int:producto_id>/', views.incrementar_cantidad, name="incrementar_cantidad"),
    path('restar_cantidad/<int:producto_id>/', views.restar_cantidad, name="restar_cantidad"),
    
]
