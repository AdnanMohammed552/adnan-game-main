# Generated by Django 4.0 on 2023-05-15 21:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0088_alter_summeryofletter_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summeryofletter',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 21, 47, 55, 583396, tzinfo=utc)),
        ),
    ]
