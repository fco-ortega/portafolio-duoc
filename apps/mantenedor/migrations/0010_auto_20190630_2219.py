# Generated by Django 2.2.1 on 2019-07-01 02:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0009_auto_20190630_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id_estado', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id_habitacion', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_cama', models.CharField(max_length=15)),
                ('accesorios', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('id_estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenedor.Estado')),
            ],
        ),
        migrations.AlterField(
            model_name='reporte',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 30, 22, 19, 43, 119234)),
        ),
        migrations.CreateModel(
            name='Huesped',
            fields=[
                ('run_huesped', models.IntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=20)),
                ('genero', models.CharField(max_length=1)),
                ('telefono_movil', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=30)),
                ('id_habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenedor.Habitacion')),
                ('rut_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenedor.Cliente')),
            ],
        ),
    ]
