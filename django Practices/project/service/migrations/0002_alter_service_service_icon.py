# Generated by Django 5.1.1 on 2024-10-07 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_icon',
            field=models.ImageField(upload_to='service_icons/'),
        ),
    ]
