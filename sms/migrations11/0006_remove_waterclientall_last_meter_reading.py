# Generated by Django 3.1.5 on 2021-09-08 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0005_auto_20210908_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waterclientall',
            name='last_meter_reading',
        ),
    ]