from django.contrib import admin
from core.models import *
from django import forms
# Register your models here.

'''class CategoriAdmin(admin.ModelAdmin):
  list_display = ('categoria', 'baja')
  list_editable = ('categoria', 'baja')
  #list_display_links = ['']
  search_fields = ['']'''

class gsAdminSite(admin.AdminSite):
  site_header = "Administración de GameShop"
  site_title = "Administración de Usuarios y Modelos"
  index_title = "Administración del sitio"
  empty_value_display = 'vacio'

"""
sitio_admin = gsAdminSite(name="gsamin")
sitio_admin.register(Persona)
sitio_admin.register(Proveedor)
sitio_admin.register(Producto)
sitio_admin.register(Categoria)
#sitio_admin.register(Categoria_Producto)
sitio_admin.register(Wishlist)
"""

class CategoriaProductoForm(forms.ModelForm):
    class Meta:
        model = Categoria_Producto
        fields = '__all__'


class CategoriaProductoInline(admin.TabularInline):
    model = Categoria.productos.through
    extra = 1
    form = CategoriaProductoForm


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    inlines = [CategoriaProductoInline]


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'proveedor', 'precio', 'stock')
    list_editable = ('descripcion', 'proveedor', 'precio', 'stock')
    list_display_links = ('nombre',)
    search_fields = ['proveedor']

admin.site.register(Wishlist)
admin.site.register(Proveedor)