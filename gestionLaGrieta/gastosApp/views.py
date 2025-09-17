from django.shortcuts import render, redirect
from .form import gastos_form
from .models import Gasto
from django.core.mail import EmailMessage
from django.urls import reverse
from inventarioApp.models import producto


# Create your views here.
def gastos (request):
    form_gastos = gastos_form()
    gastos = Gasto.objects.all().order_by('-fecha')
    return render (request, "gastos/gastos.html",{
        "form_gastos": form_gastos,
        "gastos": gastos
    })

def registro_gastos (request):
    if request.method=='POST':
        formulario_gasto=gastos_form(request.POST, request.FILES)
        producto_nuevo = 'producto_nuevo' in request.POST
        
        if formulario_gasto.is_valid():
            if producto_nuevo:
                nombre = request.POST.get('nuevo_nombre')           #obtener el nombre del nuevo producto
                if producto.objects.filter(titulo__iexact=nombre).exists():         #verificar si el producto ya existe
                    return redirect("../")
                descripcion = request.POST.get('nuevo_descripcion')
                cantidad=int(formulario_gasto.cleaned_data["cantidad"])
                imagen = request.FILES.get('nuevo_imagen')                  #obtener la imagen del nuevo producto
                if not imagen:                                              # Si no se subió imagen, usa la ruta por defecto
                    imagen = 'productos/default.png' 
                precio_unitario=formulario_gasto.cleaned_data["precio_unitario"]
                precio_total=formulario_gasto.cleaned_data["precio_total"]
                nuevo_producto = producto.objects.create(
                    
                    titulo=nombre,
                    descripcion=descripcion,
                    imagen = imagen,
                    cantidad=cantidad,
                    precio_unitario=precio_unitario,
                    precio_total=precio_total,
                )
                
                Gasto.objects.create(
                    producto=nuevo_producto,
                    cantidad=cantidad,
                    precio_unitario=precio_unitario,
                    precio_total=precio_total
                )
            else:
                produc = formulario_gasto.cleaned_data["titulo"]          #obtener el producto existente del formulario
                cantidad=int(formulario_gasto.cleaned_data["cantidad"])
                precio_unitario=formulario_gasto.cleaned_data["precio_unitario"]
                precio_total=formulario_gasto.cleaned_data["precio_total"]
                
                # Actualiza el producto en el invetario
                produc.cantidad += cantidad
                produc.precio_unitario = precio_unitario 
                produc.save()
                
            
            # Guarda el gasto en la tabla de gastos
                Gasto.objects.create(
                    producto=produc,
                    cantidad=cantidad,
                    precio_unitario=precio_unitario,
                    precio_total=precio_total
                )
            
            #enviar_correo()
            return redirect(reverse('Registro_gastos') + '?valido')
        else:
            redirect("../")
        
    return redirect("../")

            


def enviar_correo(request):
    #Obtener los datos descritos en el formulario
    nombre = request.POST.get("nombre")
    descripcion = request.POST.get("descripcion")
    cantidad = request.POST.get("cantidad")
    valor_total = request.POST.get("valor_total")
            
    #creacion de correo de datos para enviar por email
    email=EmailMessage("GastoLaGrieta","Fue registrado el gasto de: -{}-, definido como: -{}-, con la cantidad de: -{}-, con un valor de: -{}-".format(nombre,descripcion,cantidad,valor_total),
                       "", ["leitofinger@gmail.com"])
            
    #Envio de email con los datos
    try:
        email.send()
        return redirect("/gastos/?valido")
    except:
        return redirect("/gastos/?novalido")