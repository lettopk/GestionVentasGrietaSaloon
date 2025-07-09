from django.urls import path
from gestionLaGrietaApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="Inicio La Grieta"),
    path('ventas_diarias/', views.ventas_diarias, name="ventas Diarias"),
    path('ventas_semanales/', views.ventas_semanales, name="Registro ventas semanales"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)