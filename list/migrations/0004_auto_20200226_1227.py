# Generated by Django 3.0.3 on 2020-02-26 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20200226_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listm',
            name='is_important',
        ),
        migrations.RemoveField(
            model_name='listm',
            name='is_time_sensitive',
        ),
    ]
