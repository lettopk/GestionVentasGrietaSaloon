from django.shortcuts import render, redirect
from .pedido import Pedido
from inventarioApp.models import producto
from pedidosApp.models import pedido

# Create your views here.
def agregar_producto(request, producto_id):
    pedido = Pedido(request)
    producto = producto.objects.get(id=producto_id)
    pedido.agregar_producto(producto=producto)
    return redirect("Pedidos")

def agregar_producto(request, producto_id):
    pedido = Pedido(request)
    producto = producto.objects.get(id=producto_id)
    pedido.agregar_producto(producto=producto)
    return redirect("Pedidos")

def eliminar_producto(request, producto_id):
    pedido = Pedido(request)
    producto = producto.objects.get(id=producto_id)
    pedido.eliminar_producto(producto=producto)
    return redirect("Pedidos")

def restar_producto(request, producto_id):
    pedido = Pedido(request)
    producto = producto.objects.get(id=producto_id)
    pedido.restar_producto(producto=producto)
    return redirect("Pedidos")

def limpiar_pedido(request, producto_id):
    pedido = Pedido(request)
    pedido.limpiar_pedido()
    return redirect("Pedidos")


def pedidos (request):
    #pedidos = pedido.objects.all()
    productos = producto.objects.all()
    return render(request,"pedido/pedidos.html", {"productos":productos})
