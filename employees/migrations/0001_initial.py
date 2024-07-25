# Generated by Django 5.0.6 on 2024-07-25 10:40

import django.db.models.deletion
import employees.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.CharField(default=employees.models.generate_dept_id, max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.CharField(default=employees.models.generate_emp_id, max_length=10, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('hire_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('address', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('aadhar_number', models.CharField(max_length=20)),
                ('pan_number', models.CharField(max_length=20)),
                ('bank_name', models.CharField(max_length=100)),
                ('bank_account_number', models.CharField(max_length=50)),
                ('bank_ifsc_code', models.CharField(max_length=20)),
                ('is_doc_uploaded', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('pos_id', models.CharField(default=employees.models.generate_pos_id, max_length=8, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequiredDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_type', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='employee_documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='employees.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeePosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.department')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.employee')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.position')),
            ],
        ),
    ]
