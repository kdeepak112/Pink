# Generated by Django 3.0.8 on 2020-12-01 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0008_auto_20201201_2241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 1, 22, 45, 4, 297520)),
        ),
    ]
