# Generated by Django 2.2 on 2020-01-07 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20200105_1131'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='serviceRender',
            new_name='serviceProvider',
        ),
    ]