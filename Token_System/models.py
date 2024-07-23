from django.db import models

from Orders.models import Order

class Token(models.Model):
    token_number = models.CharField(max_length=50, unique=True)
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='token')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)