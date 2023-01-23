# Generated by Django 4.1.4 on 2023-01-17 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='item',
            name='is_verified',
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.FloatField(),
        ),
    ]
