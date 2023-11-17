from django import forms
from django.core.exceptions import ValidationError
from .models import Producto, Categoria, Proveedor

# --------------------------------------------------------------------------------------------------------- #

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    apellido = forms.CharField(label="Apellido", required=True)
    email = forms.EmailField(label="Email", required=True)
    telefono = forms.CharField(label="Telefono", required=True)
    mensaje = forms.CharField(widget=forms.Textarea)

    def clean_telefono(self):
        if not self.cleaned_data["telefono"].isdigit():
            raise ValidationError('El telefono debe contener solo numeros')
    
        return self.cleaned_data["telefono"]
    
    def clean_nombre(self):
        if self.cleaned_data["nombre"].isdigit():
            raise ValidationError('el nombre no debe contener numeros')
        
        return self.cleaned_data['nombre']
    
    def clean_apellido(self):
        if self.cleaned_data["apellido"].isdigit():
            raise ValidationError('el apellido no debe contener numeros')
        
        return self.cleaned_data['apellido']
            
    def clean(self):
        pass

# --------------------------------------------------------------------------------------------------------- #

class ProductoAltaForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

    categoria = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Esto permite la selección múltiple
        label="Categoría(s) del producto"
    )
    
    proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(), label="Proveedor del producto")

    def clean_precio(self):
        if self.cleaned_data["precio"] < 0:
            raise ValidationError("Ingrese un precio válido")
        
        return self.cleaned_data["precio"]
 
# --------------------------------------------------------------------------------------------------------- #































# class ProductoAltaForm(forms.Form):
#     producto = forms.CharField(label="nombre del Producto",required=True)
#     precio = forms.IntegerField(label="precio del producto",required=True)
#     descripcion = forms.CharField(label="descripcion del producto")
#     categoria = forms.ForeignKey(label="categoria") -- VER QUÉ ONDA ESTO
#     stock = forms.IntegerField(label="stock",required=True)

#     def clean_precio(self):
#         if self.cleaned_data["precio"] < 0:
#             raise ValidationError("Ingrese un precio válido")
        
#         return self.cleaned_data["precio"] 
    