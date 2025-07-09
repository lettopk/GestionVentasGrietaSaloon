from django.shortcuts import render, redirect
from .form import formulario_gastos
from django.core.mail import EmailMessage

# Create your views here.
def gastos (request):
    formulario_gasto = formulario_gastos()
    
    if request.method=='POST':
        formulario_gasto=formulario_gastos(data=request.POST)
        if formulario_gasto.is_valid():
            #Obtener los datos descritos en el formulario
            nombre = request.POST.get("nombre")
            descripcion = request.POST.get("descripcion")
            unidades = request.POST.get("unidades")
            valor_total = request.POST.get("valor_total")
            
            #creacion de correo de datos para enviar por email
            email=EmailMessage("GastoLaGrieta","Fue registrado el gasto de: -{}-, definido como: -{}-, con la cantidad de: -{}-, con un valor de: -{}-".format(nombre,descripcion,unidades,valor_total),
                               "", ["leitofinger@gmail.com"])
            
            #Envio de email con los datos
            try:
                email.send()
                return redirect("/gastos/?valido")
            except:
                return redirect("/gastos/?novalido")
            
    return render(request,"gastos/gastos.html", {"formulario_gasto":formulario_gasto})