from django.urls import path
from .views import vista_registro,cerrar_sesion, iniciar_sesion

urlpatterns = [
    path('', vista_registro.as_view(), name="autenticacion"),
    path('cerrar_sesion/', cerrar_sesion, name="cerrar_sesion"),
    path('iniciar_sesion/', iniciar_sesion, name="iniciar_sesion"),
    
    
]