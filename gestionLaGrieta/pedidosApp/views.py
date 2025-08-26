from django.shortcuts import render, redirect
from .pedido import Pedido
from inventarioApp.models import producto
from pedidosApp.models import pedido, pedido_producto,metodo_pago_pedido, metodo_pago
from .forms import pedido_form, metodo_pago_form, producto_form
from django.db.models import Sum, F, ExpressionWrapper, IntegerField

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
            ).order_by('-updated')
    
    for p in pedidos:
        productos = p.productos.all()
        p.total_productos = sum(prod.cantidad * prod.precio_unitario for prod in productos)
    
        if (p.total_pagado or 0) == p.total_productos:
            p.estado = "Pagado"
        else:
            p.estado = "Pendiente"
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
        pedido_id = request.POST.get('pedido_id')

        try:
            pedido_obj = pedido.objects.get(id=pedido_id)
        except pedido.DoesNotExist:
            return ("Producto no encontrado")

        # Inicializa el formulario con POST y el objeto pedido
        form = producto_form(request.POST)
        
        if form.is_valid():
            producto_pedido_obj = form.save(commit=False)
            producto_pedido_obj.pedido = pedido_obj
            # Obtener el producto seleccionado
            producto_id = form.cleaned_data['producto'].id
            producto_obj = producto.objects.get(id=producto_id)
            producto_pedido_obj.precio_unitario = producto_obj.precio_unitario

            producto_pedido_obj.save()
            return redirect("../")  # Redirige principal pedidos
        else:
            return render(request, 'mesa_pedido/widget_mesa_pedido.html', {
                'form': form,
                'pedido': pedido_obj,
                'mostrar_modal': True
            })

    return redirect("../")

def incrementar_cantidad(request, producto_id):
    producto_pedido = pedido_producto.objects.get(id=producto_id)
    producto_pedido.cantidad += 1
    producto_pedido.save()
    return redirect("../../")

def restar_cantidad(request, producto_id):
    producto_pedido = pedido_producto.objects.get(id=producto_id)
    if producto_pedido.cantidad > 1:
        producto_pedido.cantidad -= 1
        producto_pedido.save()
    else:
        producto_pedido.delete()  # Si quieres eliminar el producto si la cantidad llega a 0
    return redirect("../../")



