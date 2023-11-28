from django.urls import path, include
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet, basename='producto')

urlpatterns = [
    path('', views.index, name="index"),
    path('api', include(router.urls)),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('contacto', views.contacto, name="contacto"),
    path('Nosotros', views.quienesSomos, name="nosotros"),
    path('producto/alta', views.ProductoCreateView.as_view(), name="producto_alta"),
    path('producto/lista', ProductoListView.as_view(), name='producto_lista'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('producto/buscar_producto', views.buscar_producto, name="buscar_producto"),
    path('producto/delete/<int:pk>', ProductoDeleteView.as_view(), name="producto_borrar"),
    path('producto/update/<int:pk>', ProductoUpdateView.as_view(), name="producto_editar"),
    path('producto/carrito/', views.carrito, name='carrito'),
    path('producto/agregar_carrito/<int:producto_id>/', views.agregar_a_carrito, name='agregar_a_carrito'),
    path('producto/eliminar_producto_carrito/<int:producto_id>/', views.eliminar_producto_carrito, name='eliminar_producto_carrito'),
    path('producto/enviar_pedido/', EnvioCreateView.as_view(), name='enviar_pedido'),
    path('producto/confirmacion_pedido/', ConfirmacionPedidoView.as_view(), name='confirmacion_pedido'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),


]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    #path('', views., name=""),
    #path('producto/lista', views.producto_lista, name="producto_lista"),
    #path('producto/detalle/<str:nombre_producto>', views.producto_detalle, name="producto_detalle"),
    #path('producto/hay_stock', views.producto_hay_stock, {'hay_stock': 'si'} , name="hay_stock"),
    #path('producto/no_hay_stock', views.producto_hay_stock, {'hay_stock': 'no'} , name="no_hay_stock"),