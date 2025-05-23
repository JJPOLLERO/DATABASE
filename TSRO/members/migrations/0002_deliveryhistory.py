# Generated by Django 5.2.1 on 2025-05-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petroleum_name', models.CharField(max_length=100)),
                ('supplier', models.CharField(max_length=100)),
                ('delivery_code', models.CharField(max_length=20, unique=True)),
                ('date_deliver', models.DateField()),
                ('total_volume', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Delivery History',
            },
        ),
    ]
