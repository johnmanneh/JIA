# Generated by Django 3.0.8 on 2020-07-11 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jiawem', '0002_auto_20200711_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='genderField',
        ),
    ]