from django.shortcuts import render, HttpResponse

def home (request):
    return render(request,"gestionLaGrietaApp/home.html")

def ventas_diarias (request):
    return render(request,"gestionLaGrietaApp/ventas_diarias.html")

def ventas_semanales (request):
    return render(request,"gestionLaGrietaApp/ventas_semanales.html")