# Generated by Django 5.0.6 on 2024-06-01 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_vdstds_serial_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vdstds',
            options={'ordering': ['serial_number']},
        ),
    ]
