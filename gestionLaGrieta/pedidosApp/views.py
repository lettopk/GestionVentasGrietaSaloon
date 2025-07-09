from django.shortcuts import render
from pedidosApp.models import pedido

# Create your views here.
def pedidos (request):
    pedidos = pedido.objects.all()
    return render(request,"pedido/pedidos.html", {"pedidos": pedidos})