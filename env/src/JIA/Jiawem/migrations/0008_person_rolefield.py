# Generated by Django 3.0.8 on 2020-07-11 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jiawem', '0007_auto_20200711_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='roleField',
            field=models.CharField(choices=[('s', 'singer'), ('b', 'band'), ('u', 'usher'), ('d', 'deacon')], default='null', max_length=10),
        ),
    ]
