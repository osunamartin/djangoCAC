from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
#from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from .forms import ContactoForm, ProductoAltaForm
from .models import Persona, Producto, Wishlist
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
# Create your views here.

def index(request):
  context = {
    'nombre_usuario':'Juan',
    'fecha':datetime.now(),
    'es_cliente': False,
  }
  
  return render(request, "core/index.html", context)

@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required('core.add_producto', raise_exception=True), name='dispatch')
class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'core/producto_alta.html'
    context_object_name = "alta_producto_form"
    form_class = ProductoAltaForm
    success_url = reverse_lazy("producto_lista")

class ProductoListView(ListView):
    model = Producto
    template_name = 'core/producto_lista.html'  # Nombre de la plantilla HTML
    context_object_name = 'productos'
    
@method_decorator(login_required, name='dispatch')
class WishlistListView(ListView):
    model = Wishlist
    template_name = 'core/wishlist.html'  # Nombre de la plantilla HTML
    context_object_name = 'wishlist'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, 'Inicio de sesión requerido para acceder a la wish list.')
            return HttpResponse(status=403)  # Devuelve un código de acceso prohibido si no está autenticado
        return super().get(request, *args, **kwargs)

    
class CustomLoginView(LoginView):
    template_name = 'core/login.html'  # Nombre de tu plantilla de inicio de sesión

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Inicio de sesión requerido'
        return context

def buscar_producto(request):
  if request.method == "POST":
    buscado = request.POST['buscado']
    productos = Producto.objects.filter(nombre__icontains=buscado)
    return render(request, "core/buscar_producto.html", {'buscado': buscado, 'productos': productos})
  
  else:
    return render(request, "core/buscar_producto.html")

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