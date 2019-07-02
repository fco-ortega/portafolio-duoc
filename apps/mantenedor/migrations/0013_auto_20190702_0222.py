# Generated by Django 2.2.1 on 2019-07-02 06:22

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0012_auto_20190701_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden_pedido',
            name='estado',
            field=models.CharField(choices=[('A', 'Abierta'), ('E', 'Enviada'), ('R', 'Recibida')], default='A', max_length=1),
        ),
        migrations.AddField(
            model_name='orden_pedido',
            name='fecha_despacho',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reporte',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 2, 2, 21, 44, 349728)),
        ),
    ]
