# Generated by Django 4.1.4 on 2023-01-17 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
            ],
        ),
    ]
