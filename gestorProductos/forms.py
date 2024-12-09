from django import forms
from .models import Producto, Categoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre', 'descripcion')

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'precio', 'stock', 'categoria_id')
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion', 'precio', 'stock', 'categoria_id')

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'nombre', 'name': 'nombre', 'required': True}))
    descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'descripcion', 'name': 'descripcion', 'rows': 3, 'required': True}))
    precio = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'precio', 'name': 'precio', 'step': 0.01, 'min': 0, 'required': True}))
    stock = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'id': 'stock', 'name': 'stock', 'min': 0, 'required': True}))
    categoria_id = forms.ModelChoiceField(queryset=Categoria.objects.all(), widget=forms.Select(attrs={'class': 'form-select', 'id': 'categoria', 'name': 'categoria', 'required': True}))

        