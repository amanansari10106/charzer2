# Generated by Django 3.2.4 on 2021-07-08 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_alter_transaction_model_txn_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction_model',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='transaction_model',
            old_name='device_id',
            new_name='device',
        ),
        migrations.AddField(
            model_name='transaction_model',
            name='transaction_type',
            field=models.CharField(default='online', max_length=150),
        ),
        migrations.AlterField(
            model_name='transaction_model',
            name='description',
            field=models.CharField(default='No Description Available', max_length=150),
        ),
    ]
