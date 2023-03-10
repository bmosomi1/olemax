# Generated by Django 3.1.5 on 2021-10-25 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0041_auto_20211025_1713'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterPaymentReallocate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest_msisdn', models.CharField(max_length=250)),
                ('received_from', models.CharField(max_length=250)),
                ('amount', models.CharField(max_length=250, null=True)),
                ('confirmation_code', models.CharField(max_length=250, null=True)),
                ('account_number', models.CharField(max_length=250, null=True)),
                ('account_name', models.CharField(max_length=250, null=True)),
                ('balance_carried_forward', models.CharField(max_length=250, null=True)),
                ('processed', models.IntegerField(default=0, max_length=4)),
                ('ref_id', models.CharField(max_length=250, null=True)),
                ('comments', models.CharField(max_length=250, null=True)),
                ('pay_date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.waterclientall')),
            ],
        ),
    ]
