# Generated by Django 5.0.2 on 2024-03-03 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_alter_mydata_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydata',
            name='image',
            field=models.ImageField(default='', upload_to='touse/images'),
        ),
    ]
