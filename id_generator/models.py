from django.db import models
from employees.models import Employee  # Adjust the import path as per your app structure

class Identity_Card(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    card_pdf = models.FileField(upload_to='id_cards/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID Card for {self.employee.first_name} {self.employee.last_name}"
