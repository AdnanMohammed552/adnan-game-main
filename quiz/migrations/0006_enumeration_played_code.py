# Generated by Django 4.0 on 2023-05-15 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_alter_total_score_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='enumeration_played',
            name='code',
            field=models.CharField(default='', max_length=100),
        ),
    ]
