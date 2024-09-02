# Generated by Django 5.0.6 on 2024-06-01 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_users_serial_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=11, null=True, unique=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='img')),
            ],
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['serial_number']},
        ),
    ]
