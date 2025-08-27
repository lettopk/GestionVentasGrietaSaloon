from django import forms
from inventarioApp.models import producto

class gastos_form(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['titulo', 'cantidad', 'precio_unitario', 'precio_total']   
    
    def __init__(self, *args, **kwargs):
        super(gastos_form, self).__init__(*args, **kwargs)
        self.fields['titulo'].queryset = producto.objects.all()