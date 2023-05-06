# Generated by Django 4.0 on 2023-05-06 14:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0045_lang_alter_summeryofletter_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='lang',
            name='user',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='summeryofletter',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 6, 14, 38, 37, 516224, tzinfo=utc)),
        ),
    ]
