# Generated by Django 5.0.6 on 2024-07-26 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_loginsystem_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginsystem',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='loginsystem',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='loginsystem',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='loginsystem',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
    ]
