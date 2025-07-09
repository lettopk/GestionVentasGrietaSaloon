from django.shortcuts import render
from pedidosApp.models import pedido
from inventarioApp.models import producto

# Create your views here.
def pedidos (request):
    pedidos = pedido.objects.all()
    productos = producto.objects.all()
    return render(request,"pedido/pedidos.html", {"pedidos": pedidos, "productos":productos})