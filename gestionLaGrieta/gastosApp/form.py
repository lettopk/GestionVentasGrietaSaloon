from django import forms

class formulario_gastos(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    descripcion = forms.CharField(label="Descripcion", widget=forms.Textarea)
    unidades = forms.IntegerField(label="Unidades", required=True)
    valor_total= forms.IntegerField(label="Valor total", required=True)