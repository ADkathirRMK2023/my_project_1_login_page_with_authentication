# Generated by Django 4.2.4 on 2023-08-28 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actual_user_input', '0002_new_loggers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_loggers',
            name='search_period',
        ),
    ]
