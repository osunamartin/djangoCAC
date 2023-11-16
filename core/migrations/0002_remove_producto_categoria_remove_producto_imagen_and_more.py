# Generated by Django 4.2.5 on 2023-11-16 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
        migrations.AddField(
            model_name='categoria',
            name='productos',
            field=models.ManyToManyField(through='core.Categoria_Producto', to='core.producto'),
        ),
    ]