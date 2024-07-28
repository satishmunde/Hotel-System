# crmapp/models.py
from django.db import models
from core.models import LoginSystem
# from Orders.models import Order

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, primary_key=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return  f"{self.name} - {self.phone}"

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
