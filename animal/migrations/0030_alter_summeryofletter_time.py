# Generated by Django 4.0 on 2022-12-24 14:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0029_alter_summeryofletter_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summeryofletter',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 24, 14, 3, 34, 73404, tzinfo=utc)),
        ),
    ]