# Generated by Django 4.2.5 on 2023-11-28 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='producto',
        ),
        migrations.AddField(
            model_name='wishlist',
            name='productos',
            field=models.ManyToManyField(to='core.producto'),
        ),
    ]
