from django.db import models
# from Token_System.models import Token  # Adjust the import path as per your app structure

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        # Add more statuses as needed
    ]

    customer_name = models.CharField(max_length=100)
    items = models.TextField()  # JSONField or TextField to store items as JSON or text
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    # token = models.OneToOneField(Token, on_delete=models.SET_NULL, null=True, blank=True, related_name='order')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)