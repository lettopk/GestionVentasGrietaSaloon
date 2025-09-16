from django import forms
from inventarioApp.models import producto

class gastos_form(forms.ModelForm):
    titulo = forms.ModelChoiceField(queryset=producto.objects.all(), label="Producto")
    class Meta:
        model = producto
        fields = ['titulo', 'cantidad', 'precio_unitario', 'precio_total']   
    
    def __init__(self, *args, **kwargs):
        super(gastos_form, self).__init__(*args, **kwargs)
        self.fields['titulo'].queryset = producto.objects.all()