# Generated by Django 5.0.7 on 2024-08-26 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0001_initial'),
        ('core', '0003_loginsystem_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.company'),
            preserve_default=False,
        ),
    ]
