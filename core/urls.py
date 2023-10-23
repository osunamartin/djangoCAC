from django.urls import path
from . import views

urlpatterns = [
    #path('', views., name=""),
    path('', views.index, name="index"),
    path('contacto', views.contacto, name="contacto"),
    path('Nosotros', views.quienesSomos, name="nosotros"),
    path('producto/alta', views.producto_alta, name="producto_alta"),
    path('producto/lista', views.producto_lista, name="producto_lista"),
    path('producto/detalle/<str:nombre_producto>', views.producto_detalle, name="producto_detalle"),
    path('producto/hay_stock', views.producto_hay_stock, {'hay_stock': 'si'} , name="hay_stock"),
    path('producto/no_hay_stock', views.producto_hay_stock, {'hay_stock': 'no'} , name="no_hay_stock"),
] 