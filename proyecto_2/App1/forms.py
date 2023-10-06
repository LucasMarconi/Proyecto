from django import forms

class ClienteFormulario(forms.Form):
    
    nombre = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()
    
class BusquedaClinete(forms.Form):
    
    nombre = forms.CharField()