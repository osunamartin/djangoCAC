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

    def clean(self):
        cleaned_data = super().clean()
        producto = cleaned_data.get('producto')
        categoria = cleaned_data.get('categoria')

        if producto and categoria:
            # Verificar si el producto ya está asociado a la categoría
            if Categoria_Producto.objects.filter(producto=producto, categoria=categoria).exists():
                raise forms.ValidationError("El producto ya está en esta categoría")

class CategoriaProductoInline(admin.TabularInline):
    model = Categoria.productos.through
    form = CategoriaProductoForm
    extra = 1

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    inlines = [CategoriaProductoInline]

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'proveedor', 'precio', 'stock')
    list_editable = ('descripcion', 'proveedor', 'stock')
    list_display_links = ('nombre',)
    search_fields = ['nombre']

admin.site.register(Proveedor)
admin.site.register(Wishlist)
admin.site.register(Categoria_Producto)