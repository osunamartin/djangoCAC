from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    email = models.EmailField(max_length=40, verbose_name="Email")

#class Categoria(models.Model):
#    nombre = models.CharField(max_length=30, verbose_name="Nombre de la categoría")
    
    
class Producto (models.Model):
    nombre = models.CharField(max_length=100, verbose_name="nombre del producto")
    precio = models.IntegerField(verbose_name="precio")
    descripcion = models.CharField(max_length=200,null=True, verbose_name="descripcion del producto")
    categoria = models.CharField(max_length=100, verbose_name="categoria")  #deberia estar relacionada con otra tabla "categoria", hacerlo después.
    stock = models.IntegerField(verbose_name="stock")