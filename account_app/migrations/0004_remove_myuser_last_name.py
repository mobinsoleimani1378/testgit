# Generated by Django 4.2.7 on 2023-11-27 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0003_myuser_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='last_name',
        ),
    ]