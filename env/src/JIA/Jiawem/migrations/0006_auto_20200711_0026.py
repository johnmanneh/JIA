# Generated by Django 3.0.8 on 2020-07-11 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Jiawem', '0005_auto_20200711_0024'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Pastors',
            new_name='Pastor',
        ),
        migrations.RenameModel(
            old_name='Singers',
            new_name='Singer',
        ),
        migrations.RenameModel(
            old_name='Ushers',
            new_name='Usher',
        ),
    ]
