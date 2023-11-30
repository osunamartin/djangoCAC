from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
        exclude = ['usuario']

    
    proveedor = forms.ModelChoiceField(queryset=Proveedor.objects.all(), label="Proveedor del producto")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria_producto'] = forms.ModelMultipleChoiceField(
            queryset=Categoria.objects.all(),
            widget=forms.CheckboxSelectMultiple,  
            label="Categoría(s) del producto",
            required=False
        )

    def clean_precio(self):
        if self.cleaned_data["precio"] < 0:
            raise ValidationError("Ingrese un precio válido")
        
        return self.cleaned_data["precio"]
 
# --------------------------------------------------------------------------------------------------------- #

class EnvioForm(forms.ModelForm):
    class Meta:
        model = Envio
        fields = '__all__'

    def __init__(self, usuario_actual=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput() 

        if usuario_actual:
            carrito_usuario = Carrito.objects.get(usuario=usuario_actual)
            productos_en_carrito = carrito_usuario.productos.all()

            self.fields['productos'].queryset = productos_en_carrito

            # Establecer los productos como inicialmente seleccionados
            self.initial['productos'] = productos_en_carrito
        

# --------------------------------------------------------------------------------------------------------- #


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label= ('Correo electrónico'))
    username = forms.CharField(label= ('Nombre de usuario'))
    password1 = forms.CharField(
        label= ('Contraseña'),
        widget=forms.PasswordInput,
        help_text= ('La contraseña no debe ser demasiado común y debe tener al menos 8 caracteres.'),
    )
    password2 = forms.CharField(
        label= ('Confirmar contraseña'),
        widget=forms.PasswordInput,
        help_text= ('Ingresa la misma contraseña para verificar.'),
    )


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': "Tu nombre de usuario no debe contener caracteres especiales y debe tener longitud de 150 caracteres como máximo.",
            'password1': "Tu contraseña debe contener al menos 8 caracteres, no puede ser demasiado común y no puede ser puramente numérica.",
            'password2': "Ingresa la misma contraseña para verificación.",
        }
        error_messages = {
            'password2': {
                'password_mismatch': "Las contraseñas no coinciden.",
            },
        }























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
    