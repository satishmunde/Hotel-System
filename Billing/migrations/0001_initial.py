# Generated by Django 5.0.7 on 2024-07-28 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Orders', '0003_order_table_number_orderitem_extra_tip'),
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('bill_id', models.CharField(blank=True, max_length=18, primary_key=True, serialize=False)),
                ('subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.customer')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.order')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.CharField(blank=True, max_length=13, primary_key=True, serialize=False)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('payment_method', models.CharField(choices=[('credit_card', 'Credit Card'), ('upi', 'UPI'), ('bank_transfer', 'Bank Transfer'), ('cash', 'Cash')], default='cash', max_length=20)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bill', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Billing.bill')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.order')),
            ],
        ),
    ]
