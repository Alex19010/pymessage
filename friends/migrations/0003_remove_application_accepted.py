# Generated by Django 5.0.1 on 2024-02-23 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_application'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='accepted',
        ),
    ]
