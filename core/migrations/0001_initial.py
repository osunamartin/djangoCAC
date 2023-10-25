# Generated by Django 4.2.5 on 2023-10-25 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=30, verbose_name='nombre de la categoría')),
                ('baja', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria_Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona', models.CharField(max_length=30, verbose_name='Nombre de la persona')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=40, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor', models.CharField(max_length=30, verbose_name='nombre del proveedor')),
                ('telefono', models.IntegerField(verbose_name='numero de telefono')),
                ('email', models.EmailField(max_length=40, verbose_name='Email del proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=100, verbose_name='nombre del producto')),
                ('precio', models.IntegerField(verbose_name='precio')),
                ('descripcion', models.CharField(max_length=200, null=True, verbose_name='descripcion del producto')),
                ('stock', models.IntegerField(verbose_name='stock')),
                ('categoria', models.ManyToManyField(through='core.Categoria_Producto', to='core.categoria')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.proveedor')),
            ],
        ),
        migrations.AddField(
            model_name='categoria_producto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto'),
        ),
    ]