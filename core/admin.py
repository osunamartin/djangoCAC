from django.contrib import admin
from core.models import *
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

admin.site.register(Persona)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Categoria)
#sitio_admin.register(Categoria_Producto)
admin.site.register(Wishlist)