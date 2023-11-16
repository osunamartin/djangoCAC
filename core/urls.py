from django.urls import path
from . import views
from .views import ProductoListView, ProductoCreateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    #path('', views., name=""),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core/login.html'),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.index, name="index"),
    path('contacto', views.contacto, name="contacto"),
    path('wishlist', views.WishlistListView.as_view(), name="wishlist"),
    path('Nosotros', views.quienesSomos, name="nosotros"),
    path('producto/alta', views.ProductoCreateView.as_view(), name="producto_alta"),
    path('producto/lista', ProductoListView.as_view(), name='producto_lista'),
#   path('producto/lista', views.producto_lista, name="producto_lista"),
    path('producto/detalle/<str:nombre_producto>', views.producto_detalle, name="producto_detalle"),
    path('producto/hay_stock', views.producto_hay_stock, {'hay_stock': 'si'} , name="hay_stock"),
    path('producto/no_hay_stock', views.producto_hay_stock, {'hay_stock': 'no'} , name="no_hay_stock"),
    path('buscar_producto', views.buscar_producto, name="buscar_producto"),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)