# Generated by Django 3.0.8 on 2020-12-01 17:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_auto_20201201_2245'),
        ('doctor', '0002_consultsrequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=10000)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2020, 12, 1, 22, 45, 6, 886728))),
                ('status', models.CharField(default='unread', max_length=20)),
                ('from_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='patient.patient')),
                ('to_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='doctor.DoctorProfile')),
            ],
        ),
    ]