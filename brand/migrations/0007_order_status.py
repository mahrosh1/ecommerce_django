# Generated by Django 4.1.4 on 2023-01-02 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0006_rename_print_order_price_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
