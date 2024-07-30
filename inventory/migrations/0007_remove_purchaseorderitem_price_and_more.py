# Generated by Django 5.0.7 on 2024-07-30 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_purchaseorder_total_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorderitem',
            name='price',
        ),
        migrations.AddField(
            model_name='purchaseorderitem',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
