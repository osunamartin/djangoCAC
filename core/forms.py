from django import forms
from django.core.exceptions import ValidationError

def validate_phone_number(value):
    if not value.isdigit():
        raise ValidationError('El teléfono debe contener solo números.')

class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre de contacto", required=True)
    apellido = forms.CharField(label="Apellido de contacto", required=True)
    email = forms.EmailField(label="Email", required=True)
    telefono = forms.CharField(label="Teléfono", required=True, validators=[validate_phone_number])
    mensaje = forms.CharField(widget=forms.Textarea)