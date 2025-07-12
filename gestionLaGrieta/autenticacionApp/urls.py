from django.urls import path
from .views import vista_registro

urlpatterns = [
    path('', vista_registro.as_view(), name="autenticacion"),
    
]