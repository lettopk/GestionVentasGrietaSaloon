from django.shortcuts import render

# Create your views here.

def registro_ventas (request):
    return render(request,"registro_ventas/registro_ventas.html")