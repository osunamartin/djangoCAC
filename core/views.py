from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from datetime import datetime
from .forms import ContactoForm,ProductoAltaForm
from .models import Persona, Producto
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
# Create your views here.

def index(request):
  context = {
    'nombre_usuario':'Juan',
    'fecha':datetime.now(),
    'es_cliente': False,
  }
  
  return render(request, "core/index.html", context)


class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'core/producto_alta.html'
    context_object_name = "alta_producto_form"
    form_class = ProductoAltaForm
    success_url = reverse_lazy("producto_lista")


def producto_lista(request):
  context = {
    'nombre_usuario': 'Juan',
    'hay_stock': True,
  }
  return render(request, 'core/producto_lista.html', context)


def producto_detalle(request, nombre_producto):
  return HttpResponse(
    f"""
    <h1>Bienvenido {nombre_producto} </h1>
    <p>Detalle del producto</p>
    """
  )


def producto_hay_stock(request, hay_stock):

  return HttpResponse(f'¿Hay stock de este producto?: {hay_stock}') 

def ProductoListView(ListView):
  model = Producto
  context_object_name = 'productos'
  template_name = 'core/producto_lista.html'
  ordering = ['stock']


def contacto(request):

  if request.method == 'POST':
    # Instanciamos un formulario con datos
    formulario = ContactoForm(request.POST)

    # Validacion
    if formulario.is_valid():
      # Dar de alta la info

      nueva_persona = Persona(
        nombre = formulario.cleaned_data['nombre'],
        apellido = formulario.cleaned_data['apellido'],
        email = formulario.cleaned_data['email'],
      )

      nueva_persona.save()

      messages.info(request, "Consulta enviada con exito")
      return redirect(reverse("index"))

    
  else: # GET
    formulario = ContactoForm()

  
  context = {
    'contacto_form': formulario
  }
  
  return render(request, 'core/formContacto.html', context)


def quienesSomos(request):

  return render(request, 'core/quienesSomos.html')


'''
  Checkear esto, para que se den de alta y se creen así las vistas:

  class ProductoCreateView(CreateView):
    model = Producto
    context_object_name = ''
    template_name = 'core/producto_alta.html'
    sucess_url = 'producto_lista'
    form_class = AltaProductoModelForm

class ProductoListView (ListView):
  model = Producto
  context_object_name = ''
  template_name = 'core/productos_lista.html'''

  