# Generated by Django 4.1.3 on 2023-06-10 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0015_alter_incoming_info_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incoming_info',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
