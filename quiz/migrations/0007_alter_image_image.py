# Generated by Django 4.0 on 2023-05-16 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='3906412_LHEQA3A.png', upload_to='images/'),
        ),
    ]