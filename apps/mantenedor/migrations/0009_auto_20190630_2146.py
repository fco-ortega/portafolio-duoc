# Generated by Django 2.2.1 on 2019-07-01 01:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantenedor', '0008_reporte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporte',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 30, 21, 46, 30, 773200)),
        ),
    ]
