# Generated by Django 2.2.1 on 2019-07-02 04:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0012_auto_20190701_2345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_huesped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run_huesped', models.CharField(max_length=12)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('fecha_ingreso', models.DateField()),
                ('fecha_egreso', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='huesped',
            name='run_huesped',
            field=models.CharField(max_length=12, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='fecha',
            field=models.DateField(default=datetime.date(2019, 7, 2)),
        ),
    ]
