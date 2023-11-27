# Generated by Django 4.2.5 on 2023-11-27 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='mensaje',
            field=models.CharField(default='ninguno', max_length=250, verbose_name='Mensaje'),
        ),
        migrations.AddField(
            model_name='persona',
            name='telefono',
            field=models.IntegerField(default=0, verbose_name='Telefono'),
        ),
    ]