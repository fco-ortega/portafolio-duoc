# Generated by Django 2.2.1 on 2019-07-02 03:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0011_auto_20190630_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte',
            name='fecha',
            field=models.DateField(default=datetime.date(2019, 7, 1)),
        ),
    ]
