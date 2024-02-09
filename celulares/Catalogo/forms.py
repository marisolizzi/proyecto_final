from django import forms
from Catalogo.models import Marca

class FormMarca(forms.Form):
    nombre = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Nombre','class':'form-control'}))
    detalle = forms.CharField(required=False,widget=forms.Textarea(attrs={'placeholder':'Descripción','class':'form-control'}))
    imagen = forms.ImageField(required=False,widget=forms.FileInput(attrs={'placeholder':'Imagen','class':'form-control'}))

class FormCelular(forms.Form):
   nombre = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder':'Nombre','class':'form-control'}))
   detalle = forms.CharField(required=False,widget=forms.Textarea(attrs={'placeholder':'Descripción','class':'form-control'}))
   imagen = forms.ImageField(required=False,widget=forms.FileInput(attrs={'placeholder':'Imagen','class':'form-control'}))
   CHOICES = (('Option 1', 'Option 1'),('Option 2', 'Option 2'),)

   marcas_choice = list()
   marcas = Marca.objects.all().order_by('nombre')
   for marca in marcas:
    marcas_choice.append((marca.id,marca.nombre))
    
   categoria = forms.ChoiceField(choices=marcas_choice,widget=forms.Select(attrs={'class':'form-control'})) 



