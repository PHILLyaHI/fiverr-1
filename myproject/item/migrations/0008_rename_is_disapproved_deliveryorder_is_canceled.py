# Generated by Django 4.1.4 on 2023-01-18 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_deliveryorder_is_disapproved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deliveryorder',
            old_name='is_disapproved',
            new_name='is_canceled',
        ),
    ]