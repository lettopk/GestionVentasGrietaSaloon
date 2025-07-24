from django import forms 
from .models import pedido, metodo_pago
from django.contrib.auth.models import User

class pedido_form(forms.ModelForm):
    class Meta:
        model= pedido
        fields = ['mesa', 'vendedor', 'metodos_pago']
        
    
    def __init__(self, *args, **kwargs):
        super(pedido_form, self).__init__(*args, **kwargs)
        self.fields['vendedor'].queryset = User.objects.all()
        self.fields['metodos_pago'].queryset = metodo_pago.objects.all()