# Generated by Django 4.0 on 2022-10-29 13:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0018_alter_summeryofletter_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summeryofletter',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 29, 13, 9, 50, 374269, tzinfo=utc)),
        ),
    ]
