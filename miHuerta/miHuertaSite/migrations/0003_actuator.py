# Generated by Django 2.0 on 2020-04-29 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miHuertaSite', '0002_auto_20200422_0445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperatureActuator', models.BooleanField()),
                ('moistureActuator', models.BooleanField()),
                ('luxActuator', models.BooleanField()),
            ],
        ),
    ]