# Generated by Django 5.0.6 on 2024-05-12 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
    ]
