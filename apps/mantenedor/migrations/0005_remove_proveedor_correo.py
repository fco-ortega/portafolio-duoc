# Generated by Django 2.2.1 on 2019-06-29 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0004_empleado_orden_pedido_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='correo',
        ),
    ]