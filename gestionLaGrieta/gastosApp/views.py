from django.shortcuts import render, redirect
from .form import gastos_form
from django.core.mail import EmailMessage
from inventarioApp.models import producto

# Create your views here.
def gastos (request):
    form_gastos = gastos_form()
    productos = producto.objects.all()
    return render (request, "gastos/gastos.html",{
        "form_gastos": form_gastos,
        "productos": productos
    })

def registro_gastos (request):
    formulario_gasto = gastos_form()
    productos = producto.objects.all()
    
    if request.method=='POST':
        formulario_gasto=gastos_form(data=request.POST)
        if formulario_gasto.is_valid():
            enviar_correo(request, formulario_gasto)
            gastos_form.save()                         #Guarda los valores en la tabla
            return redirect("../")
        else:
            return render(request,"forms/registro_gasto.html", {
                "formulario_gasto":formulario_gasto, 
                "productos": productos
                })
        
    return redirect("../")

            


def enviar_correo(request, formulario_gasto):
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