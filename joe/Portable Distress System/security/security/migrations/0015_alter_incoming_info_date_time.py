# Generated by Django 4.1.3 on 2023-06-10 11:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0014_alter_friend_requests_user_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incoming_info',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 10, 11, 19, 27, 474946, tzinfo=datetime.timezone.utc)),
        ),
    ]