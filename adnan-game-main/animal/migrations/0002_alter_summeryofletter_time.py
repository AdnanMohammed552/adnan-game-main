# Generated by Django 4.0 on 2022-08-25 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summeryofletter',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 25, 19, 54, 37, 767215)),
        ),
    ]
