# Generated by Django 4.2.4 on 2023-08-29 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actual_user_input', '0003_remove_new_loggers_search_period'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new_loggers',
            old_name='password',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='new_loggers',
            name='username',
        ),
    ]