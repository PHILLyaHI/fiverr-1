# Generated by Django 4.1.4 on 2023-01-18 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0006_deliveryorder_is_approved_deliveryorder_is_completed_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryorder',
            name='is_disapproved',
            field=models.BooleanField(default=False),
        ),
    ]
