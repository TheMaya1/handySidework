# Generated by Django 2.2 on 2020-01-01 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='i_will_be_available_in',
            field=models.CharField(default=True, max_length=250),
        ),
    ]