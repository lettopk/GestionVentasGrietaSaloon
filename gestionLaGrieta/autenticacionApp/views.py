from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm 
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.

#vista para registro de usuario
class vista_registro(View):
    
    def get(self,request):
        form = UserCreationForm()                                      #Crea formulario
        return render(request, "registro/registro.html", {"form":form})#Renderiza el formulario
    
    def post(self, request):
        form = UserCreationForm(request.POST)                           #Validacion de un formulario correcto
        if form.is_valid():                  
            usuario = form.save()
            login(request, usuario)
            return redirect("Inicio La Grieta")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                
            return render(request, "registro/registro.html", {"form": form})

#vista para cierre de sesion        
def cerrar_sesion(request):
    logout(request)
    
    return redirect("Inicio La Grieta")

#vista para inicio de sesion
def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)                                    #Validacion de un formulario correcto
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contrasenia = form.cleaned_data.get("password")
            
            usuario = authenticate(username = nombre_usuario, password = contrasenia)               #Validacion de usuario y contrasenia
            if usuario is not None:
                login(request, usuario)
                return redirect("Inicio La Grieta")
            else:
                messages.error(request, "usuario no valido")
        else: 
            messages.error(request, "Información incorrecta")
    form = AuthenticationForm()
    return render(request, "inicio_sesion/inicio_sesion.html", {"form":form})
    