# Generated by Django 4.0 on 2022-08-31 13:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0009_alter_summeryofletter_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summeryofletter',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 31, 17, 16, 19, 825734)),
        ),
    ]
