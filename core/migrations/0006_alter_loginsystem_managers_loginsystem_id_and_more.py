# Generated by Django 5.0.6 on 2024-07-26 07:19

import core.models
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_loginsystem_managers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='loginsystem',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='loginsystem',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='loginsystem',
            name='emp_id',
            field=models.CharField(default=core.models.generate_emp_id, max_length=11, unique=True),
        ),
    ]
