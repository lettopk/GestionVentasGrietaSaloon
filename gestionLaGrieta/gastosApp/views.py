from django.shortcuts import render, redirect
from .form import gastos_form
from .models import Gasto
from django.core.mail import EmailMessage
from inventarioApp.models import producto

# Create your views here.
def gastos (request):
    form_gastos = gastos_form()
    gastos = Gasto.objects.all().order_by('-fecha')
    registro_gastos(request)
    return render (request, "gastos/gastos.html",{
        "form_gastos": form_gastos,
        "gastos": gastos
    })

def registro_gastos (request):
    if request.method=='POST':
        formulario_gasto=gastos_form(data=request.POST)
        
        if formulario_gasto.is_valid():
            producto=formulario_gasto.cleaned_data["titulo"]
            cantidad=int(formulario_gasto.cleaned_data["cantidad"])
            precio_unitario=formulario_gasto.cleaned_data["precio_unitario"]
            precio_total=formulario_gasto.cleaned_data["precio_total"]
            
            # Actualiza el producto en el invetario
            producto.cantidad += cantidad
            producto.precio_unitario = precio_unitario 
            producto.save()
            
            # Guarda el gasto en la tabla de gastos
            Gasto.objects.create(
                producto=producto,
                cantidad=cantidad,
                precio_unitario=precio_unitario,
                precio_total=precio_total
            )
            
            #enviar_correo()
            return redirect("../")
        else:
            formulario_gasto = gastos_form()
            return render(request,"forms/registro_gasto.html", {
                "formulario_gasto":formulario_gasto
                })
        
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