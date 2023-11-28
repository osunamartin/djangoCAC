from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=30, verbose_name="Nombre de la persona")
    apellido = models.CharField(max_length=30, verbose_name="Apellido")
    telefono = models.CharField(max_length=15, verbose_name='Telefono', default=0)
    email = models.EmailField(max_length=40, verbose_name="Email")
    mensaje = models.CharField(max_length=250, verbose_name='Mensaje', default='ninguno')


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
    stock = models.IntegerField(verbose_name="stock")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/',blank=True, null=True, verbose_name="Imagen del producto")

    def __str__(self):
        return self.nombre
    

class Categoria(models.Model):
    categoria = models.CharField(max_length=30, verbose_name="nombre de la categoría")
    baja = models.BooleanField(default=False)
    productos = models.ManyToManyField(Producto, through='Categoria_Producto')

    def __str__(self):
        return self.categoria
    

class Categoria_Producto (models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


class Wishlist(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)


class Envio(models.Model):
    nombre_completo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    pais = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)
    direccion_entrega = models.CharField(max_length=255)
    notas_pedido = models.TextField(blank=True)

    OPCIONES_ENVIO = [
        ('tienda', 'Retiro en tienda'),
        ('domicilio', 'Envío a domicilio'),
    ]

    OPCIONES_PAGO = [
        ('transferencia', 'Transferencia'),
        ('mercadopago', 'MercadoPago'),
        ('efectivo', 'Efectivo'),
    ]

    tipo_envio = models.CharField(
        max_length=10,
        choices=OPCIONES_ENVIO,
        default='tienda',
    )

    metodo_pago = models.CharField(
        max_length=15,
        choices=OPCIONES_PAGO,
        default='transferencia',
    )

    def __str__(self):
        return f"Pedido de {self.nombre_completo}"



