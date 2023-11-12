from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Persona(models.Model):
    persona = models.CharField(max_length=30, verbose_name="Nombre de la persona")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    email = models.EmailField(max_length=40, verbose_name="Email")

class Categoria(models.Model):
    categoria = models.CharField(max_length=30, verbose_name="nombre de la categoría")
    baja = models.BooleanField(default=False)

    def __str__(self):
        return self.categoria
    
class Proveedor(models.Model):
    proveedor = models.CharField(max_length=30, verbose_name="nombre del proveedor")
    telefono = models.IntegerField(verbose_name="numero de telefono")
    email = models.EmailField(max_length=40, verbose_name="Email del proveedor")

    def __str__(self):
        return self.proveedor  
    
class Producto (models.Model):
    nombre = models.CharField(max_length=100, verbose_name="nombre del producto")
    precio = models.IntegerField(verbose_name="precio")
    descripcion = models.CharField(max_length=200,null=True, verbose_name="descripcion del producto")
    categoria = models.ManyToManyField(Categoria, through='Categoria_Producto')
    stock = models.IntegerField(verbose_name="stock")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/', null=False, verbose_name="Imagen del producto")

    def __str__(self):
        return self.nombre


class Categoria_Producto (models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.categoria

class Wishlist(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE) #a qué persona está asociada la lista de deseados


    





