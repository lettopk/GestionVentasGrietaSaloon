from django.shortcuts import render, HttpResponse

def home (request):
    return render(request,"gestionLaGrietaApp/home.html")

def gastos (request):
    return render(request,"gestionLaGrietaApp/gastos.html")

def registro_ventas (request):
    return render(request,"gestionLaGrietaApp/registro_ventas.html")

def ventas_diarias (request):
    return render(request,"gestionLaGrietaApp/ventas_diarias.html")

def ventas_semanales (request):
    return render(request,"gestionLaGrietaApp/ventas_semanales.html")