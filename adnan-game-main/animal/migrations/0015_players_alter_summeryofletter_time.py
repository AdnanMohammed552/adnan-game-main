# Generated by Django 4.0 on 2022-09-22 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal', '0014_alter_array_status_alter_summeryofletter_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('players', models.CharField(max_length=900000)),
                ('room', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='summeryofletter',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 22, 20, 28, 32, 601270)),
        ),
    ]
