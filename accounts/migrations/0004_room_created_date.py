# Generated by Django 4.0 on 2023-03-29 12:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_played'),
    ]

    operations = [
        migrations.AddField(
            model_name='room_created',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
