# Generated by Django 4.1.4 on 2023-01-22 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0015_delete_invoice_remove_deliveryorder_invoice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryorder',
            name='invoice',
            field=models.IntegerField(default=0),
        ),
    ]
