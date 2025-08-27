from django.urls import path
from . import views

urlpatterns = [
    path('', views.gastos, name="Gastos"),
    path('registro_gastos/', views.registro_gastos, name="Registro_gastos"),
    
]