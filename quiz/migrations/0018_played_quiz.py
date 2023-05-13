# Generated by Django 4.0 on 2023-05-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0017_priv'),
    ]

    operations = [
        migrations.CreateModel(
            name='played_quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('code', models.IntegerField(max_length=100, unique=True)),
            ],
        ),
    ]