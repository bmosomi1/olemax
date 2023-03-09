# Generated by Django 2.2.4 on 2019-12-19 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0020_auto_20191203_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outgoing1',
            name='sent_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='CustomerTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_id', models.CharField(max_length=250, unique=True)),
                ('status_complete', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Customer')),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]