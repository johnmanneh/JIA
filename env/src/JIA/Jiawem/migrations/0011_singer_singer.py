# Generated by Django 3.0.8 on 2020-07-11 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Jiawem', '0010_remove_singer_singer'),
    ]

    operations = [
        migrations.AddField(
            model_name='singer',
            name='singer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Jiawem.Person'),
            preserve_default=False,
        ),
    ]
