from django.shortcuts import render, redirect
from .pedido import Pedido
from inventarioApp.models import producto
from pedidosApp.models import pedido, pedido_producto,metodo_pago_pedido, metodo_pago
from .forms import pedido_form, metodo_pago_form

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
        print("POST DATA:", request.POST)
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
            return redirect("../")  # Redirige donde sea necesario
        else:
            return render(request, 'mesa_pedido/widget_mesa_pedido.html', {
                'form': form,
                'pedido': pedido_obj,
                'mostrar_modal': True
            })

    return redirect("../")



def agregar_producto(request, producto_id):
    pedido = Pedido(request)
    producto = producto.objects.get(id=producto_id)
    pedido.agregar_producto(producto=producto)
    return redirect("Pedidos")

def agregar_producto(request,producto_id):
    
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad'))
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
    productos_base = producto.objects.all()
    productos = pedido_producto.objects.all()
    metodos_pago = metodo_pago.objects.all()
    form = pedido_form()
    formp = metodo_pago_form()
    return render(request,"pedido/pedidos.html", {"productos":productos,"productos_base":productos_base,"pedidos":pedidos, 'form':form, "metodos_pago":metodos_pago, 'formp':formp})
