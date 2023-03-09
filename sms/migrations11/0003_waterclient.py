# Generated by Django 3.1.5 on 2021-09-08 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_waterclients'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=250)),
                ('phone_number', models.CharField(max_length=250)),
                ('client_number', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('kra_pin', models.CharField(max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]