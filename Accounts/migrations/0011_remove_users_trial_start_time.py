# Generated by Django 5.0.6 on 2024-06-29 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0010_users_trial_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='trial_start_time',
        ),
    ]
