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
    items = models.TextField()  
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.customer_name} -  {self.total_amount} - {self.status}"
    

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()