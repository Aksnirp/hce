# Generated by Django 5.0.6 on 2024-05-12 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_remove_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(default=0, max_length=100),
        ),
    ]
