# Generated by Django 4.1.3 on 2023-06-05 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0011_friend_requests'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend_requests',
            name='date',
            field=models.DateTimeField(default='1111-11-11'),
        ),
    ]
