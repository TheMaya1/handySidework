# Generated by Django 2.2 on 2020-01-05 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerender',
            name='are_you_available',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='servicerender',
            name='location',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]