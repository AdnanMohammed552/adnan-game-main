# Generated by Django 4.0 on 2023-05-09 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='delete',
            field=models.BooleanField(default=False),
        ),
    ]