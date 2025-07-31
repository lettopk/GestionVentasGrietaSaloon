from django.shortcuts import render, redirect
from .pedido import Pedido
from inventarioApp.models import producto
from pedidosApp.models import pedido, pedido_producto,metodo_pago_pedido, metodo_pago
from .forms import pedido_form, metodo_pago_form, producto_form
from django.db.models import Sum, F, ExpressionWrapper, IntegerField

# Create your views here.
def crear_pedido(request):
    if request.method == "POST":
        form = pedido_form(request.POST)        #Guarda el formulario de creacion
        if form.is_valid():
            form.save()                         #Guarda los valores en la tabla
            return redirect("../")
        else:
            return render(request, 'mesa_pedido/widget_mesa_pedido.html', {'form':form, 'mostrar_modal':True} )
        
    return redirect("../")

def agregar_metodo_pago(request):
    if request.method == "POST":
        pedido_id = request.POST.get('pedido_id')

        try:
            pedido_obj = pedido.objects.get(id=pedido_id)
        except pedido.DoesNotExist:
            return ("Pedido no encontrado")

        # Inicializa el formulario con POST y el objeto pedido
        form = metodo_pago_form(request.POST)
        
        if form.is_valid():
            metodo_pago_pedido_obj = form.save(commit=False)
            metodo_pago_pedido_obj.pedido = pedido_obj
            metodo_pago_pedido_obj.save()
            return redirect("../")  # Redirige principal pedidos
        else:
            return render(request, 'mesa_pedido/widget_mesa_pedido.html', {
                'form': form,
                'pedido': pedido_obj,
                'mostrar_modal': True
            })

    return redirect("../")



def agregar_producto(request):
    if request.method == "POST":
        print("POST DATA:", request.POST)
        producto_id = request.POST.get('producto_id')

        try:
            producto_obj = producto.objects.get(id=producto_id)
        except producto.DoesNotExist:
            return ("Producto no encontrado")

        # Inicializa el formulario con POST y el objeto pedido
        form = producto_form(request.POST)
        
        if form.is_valid():
            producto_pedido_obj = form.save(commit=False)
            producto_pedido_obj.pedido = producto_obj
            producto_pedido_obj.save()
            return redirect("../")  # Redirige principal pedidos
        else:
            return render(request, 'mesa_pedido/widget_mesa_pedido.html', {
                'form': form,
                'pedido': producto_obj,
                'mostrar_modal': True
            })

    return redirect("../")
        
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
    productos_base = producto.objects.all()
    productos = pedido_producto.objects.all()
    metodos_pago = metodo_pago.objects.all()
    metodos_pago_pedido = metodo_pago_pedido.objects.all()
    form = pedido_form()
    formp = metodo_pago_form()
    formpr = producto_form()
    pedidos = pedido.objects.annotate(
            total_pagado=Sum('metodo_pago__valor')
            )
    
    for p in pedidos:
        productos = p.productos.all()
        p.total_productos = sum(prod.cantidad * prod.precio_unitario for prod in productos)
    print(pedidos)
    return render(request,"pedido/pedidos.html", 
                  {"productos":productos,
                  "productos_base":productos_base,
                  "pedidos":pedidos,
                  "metodos_pago":metodos_pago, 
                  "metodos_pago_pedido":metodos_pago_pedido, 
                  'form':form,
                  'formp':formp, 
                  'formpr':formpr, 
                  })
