# Generated by Django 3.0.8 on 2020-07-11 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jiawem', '0006_auto_20200711_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='genderField',
            field=models.CharField(choices=[('1', ' '), ('2', 'Male'), ('3', 'Female')], default='null', max_length=6),
        ),
    ]
