# Generated by Django 4.0 on 2022-08-31 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='startingroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.CharField(max_length=150)),
                ('started', models.BooleanField()),
                ('end', models.BooleanField()),
            ],
        ),
    ]
