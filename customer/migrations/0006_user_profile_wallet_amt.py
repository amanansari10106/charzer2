# Generated by Django 3.2.4 on 2021-07-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20210626_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='wallet_amt',
            field=models.FloatField(default=0),
        ),
    ]
