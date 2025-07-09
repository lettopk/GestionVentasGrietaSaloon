from django.shortcuts import render

from inventarioApp.models import producto

# Create your views here.
def inventario (request):
    
    productos = producto.objects.all()
    return render(request,"inventario/inventarios.html", {"productos" : productos})