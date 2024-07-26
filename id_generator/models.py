from django.db import models
from django.conf import settings


class Identity_Card(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    card_pdf = models.FileField(upload_to='id_cards/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"ID Card for {self.employee.first_name} {self.employee.last_name}"
    
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
