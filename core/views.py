from django.http import Http404
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from .forms import *
from rest_framework import viewsets
from .serializers import ProductoSerializer
from .models import *
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.views import LoginView 
from django.db.models import Sum
from django.views.generic import TemplateView



# ---------------------------------------------------- #

def index(request):
  context = {
    'nombre_usuario':'Juan',
    'fecha':datetime.now(),
    'es_cliente': False,
  }

  return render(request, "core/index.html", context)

# -------------------- Login -------------------------------- #

class CustomLoginView(LoginView):
    template_name = 'core/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Inicio de sesión requerido'
        return context

# -------------------- Contacto -------------------------------- #

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
        telefono = formulario.cleaned_data['telefono'],
        email = formulario.cleaned_data['email'],
        mensaje = formulario.cleaned_data['mensaje']
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

# --------------------------------- Registro de usuarios-------------------------------------#

def register(response):
   if response.method == "POST":
      form = RegisterForm(response.POST)
      if form.is_valid():
         form.save()
      
      return redirect('/game_shop/')
   else:
    form = RegisterForm()
   
   return render(response, 'core/register.html', {'form':form})

# ------------------------------------- Nosotros ------------------------------------------- #

def quienesSomos(request):

  return render(request, 'core/quienesSomos.html')

# ------------------------------------ Productos --------------------------------- #

@method_decorator(login_required, name='dispatch')
@method_decorator(permission_required('core.add_producto'), name='dispatch')
class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'core/producto_alta.html'
    context_object_name = "alta_producto_form"
    form_class = ProductoAltaForm
    success_url = reverse_lazy("producto_lista")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()

        # Obtén las categorías seleccionadas del formulario
        categorias = form.cleaned_data['categoria_producto']

        # Agrega cada categoría al producto
        for categoria in categorias:
            Categoria_Producto.objects.create(producto=self.object, categoria=categoria)

        return super().form_valid(form)


class ProductoListView(ListView):
  model = Producto
  template_name = 'core/producto_lista.html'
  context_object_name = 'productos'

  def get_queryset(self):
    categoria_id = self.request.GET.get('categoria')
    queryset = super().get_queryset()
    if categoria_id:
      queryset = queryset.filter(categoria__id=categoria_id)
    return queryset

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['categorias'] = Categoria.objects.all()  # Obtener todas las categorías
    return context

    
def buscar_producto(request):
  if request.method == "POST":
    buscado = request.POST['buscado']
    productos = Producto.objects.filter(nombre__icontains=buscado)
    return render(request, "core/buscar_producto.html", {'buscado': buscado, 'productos': productos})
  
  else:
    return render(request, "core/buscar_producto.html")
  

class ProductoDeleteView(DeleteView):
  model = Producto
  success_url = reverse_lazy("producto_lista")


class ProductoUpdateView(UpdateView):
  model = Producto 
  fields = ['nombre', 'precio', 'stock', 'imagen']
  success_url = reverse_lazy("producto_lista")


def detalle_producto(request, producto_id):
    try:
        producto = get_object_or_404(Producto, pk=producto_id)
        context = {
            'producto': producto
            # Agrega aquí cualquier otro contexto necesario para tu template
        }
        return render(request, 'core/detalle_producto.html', context)
    except Producto.DoesNotExist:
        raise Http404("El producto no existe")


# ---------------------------------------------------------------------------------- #

class ProductoViewSet(viewsets.ModelViewSet):
   queryset = Producto.objects.all()
   serializer_class = ProductoSerializer

# ----------------------------------------------- carrito ------------------------------------------------------------------- #

@login_required
def carrito(request):
    usuario_actual = request.user
    carrito_productos = Carrito.objects.filter(usuario=usuario_actual)
    
    # Calcular el precio total de los productos en la carrito
    precio_total = carrito_productos.aggregate(total=Sum('productos__precio'))['total']
    
    context = {
        'carrito_productos': carrito_productos,
        'precio_total': precio_total if precio_total else 0  # Manejar el caso de que no haya productos
    }
    
    return render(request, 'core/carrito.html', context)


@login_required
def agregar_a_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    usuario_actual = request.user

    carrito, created = Carrito.objects.get_or_create(usuario=usuario_actual)

    if producto not in carrito.productos.all():
        carrito.productos.add(producto)
        carrito.save()

    return redirect('carrito')


@login_required
def eliminar_producto_carrito(request, producto_id):
    usuario_actual = request.user
    carrito = Carrito.objects.get(usuario=usuario_actual)
    producto_a_eliminar = Producto.objects.get(pk=producto_id)
    
    if producto_a_eliminar in carrito.productos.all():
        carrito.productos.remove(producto_a_eliminar)
    
    return redirect('carrito')

# --------------------------------------------- Proceso compra --------------------------------------------------------------------- #

class EnvioCreateView(CreateView):
    model = Envio
    form_class = EnvioForm
    template_name = 'core/formulario_envio.html'
    success_url = reverse_lazy("confirmacion_pedido")

    def form_valid(self, form):
        return super().form_valid(form)
    
class ConfirmacionPedidoView(TemplateView):
    template_name = 'core/confirmacion_pedido.html'

# ------------------------------------------------------------------------------------------------------------------ #






























# @method_decorator(login_required, name='dispatch')
# class carritoListView(ListView):
#     model = carrito
#     template_name = 'core/carrito.html' 
#     context_object_name = 'carrito'


# def producto_lista(request):
#   context = {
#     'nombre_usuario': 'Juan',
#     'hay_stock': True,
#   }
#   return render(request, 'core/producto_lista.html', context)
 
# ---------------------------------------------------------------------- #

# def producto_hay_stock(request, hay_stock):

#   return HttpResponse(f'¿Hay stock de este producto?: {hay_stock}') 

# ------------------------------------------------------------------------- #

# def producto_detalle(request, nombre_producto):
#   return HttpResponse(
#     f"""
#     <h1>Bienvenido {nombre_producto} </h1>
#     <p>Detalle del producto</p>
#     """
#   )