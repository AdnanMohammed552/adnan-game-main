# Generated by Django 4.0 on 2022-08-31 13:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0007_alter_summeryofletter_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='startingroom',
        ),
        migrations.AlterField(
            model_name='summeryofletter',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 31, 17, 10, 20, 588489)),
        ),
    ]
