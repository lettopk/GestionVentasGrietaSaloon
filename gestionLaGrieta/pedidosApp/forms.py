from django import forms 
from .models import pedido, metodo_pago_pedido,metodo_pago ,pedido_producto
from inventarioApp.models import producto
from django.contrib.auth.models import User

class pedido_form(forms.ModelForm):
    class Meta:
        model= pedido
        fields = ['mesa', 'vendedor']    
        
    def __init__(self, *args, **kwargs):
        super(pedido_form, self).__init__(*args, **kwargs)
        self.fields['vendedor'].queryset = User.objects.all()
        
        
class metodo_pago_form(forms.ModelForm):
    class Meta:
        model = metodo_pago_pedido
        fields = ['metodo_pago', 'valor']
        
    def __init__(self, *args, **kwargs):
        super(metodo_pago_form, self).__init__(*args, **kwargs)
        self.fields['metodo_pago'].queryset = metodo_pago.objects.all()
        self.pedido = pedido


class producto_form(forms.ModelForm):
    class Meta:
        model = pedido_producto
        fields = ['producto', 'cantidad']
        
    def __init__(self, *args, **kwargs):
        super(producto_form, self).__init__(*args, **kwargs)
        self.fields['producto'].queryset = producto.objects.all()
        self.pedido = pedido