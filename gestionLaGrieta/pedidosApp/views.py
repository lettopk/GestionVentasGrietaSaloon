from django.shortcuts import render, redirect
from .pedido import Pedido
from inventarioApp.models import producto
from pedidosApp.models import pedido, pedido_producto

# Create your views here.
def agregar_producto(request, producto_id):
    pedido = Pedido(request)
    producto = producto.objects.get(id=producto_id)
    
    print(producto.id)
    pedido.agregar_producto(producto=producto)
    return redirect("Pedidos")

def agregar_producto(request):
    
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad'))
        print(producto_id,cantidad)

        producto = producto.objects.get(id=producto_id)

        total = producto.precio_unitario * cantidad

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
    pedidos = pedido.objects.all()
    productos = pedido_producto.objects.all()
    return render(request,"pedido/pedidos.html", {"productos":productos,"pedidos":pedidos})
