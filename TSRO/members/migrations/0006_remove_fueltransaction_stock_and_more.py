# Generated by Django 5.2.1 on 2025-05-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_fueltransaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fueltransaction',
            name='stock',
        ),
        migrations.AlterField(
            model_name='fueltransaction',
            name='fuel_type',
            field=models.CharField(choices=[('Unleaded', 'Unleaded'), ('Diesel', 'Diesel'), ('Premium', 'Premium'), ('V-Power', 'V-Power'), ('XCS', 'XCS'), ('Xtra', 'Xtra')], max_length=20),
        ),
    ]
