from django.conf import settings
from django.utils import timezone
from django.db import models
from crm.models import Customer
from menu.models import MenuItem  # Assuming Item model is defined in menu app
from django.conf import settings
from django.db import models
from django.utils import timezone
from menu.models import MenuItem
from crm.models import Customer


def generate_order_id():
    today = timezone.localdate()
    formatted_date = today.strftime('%y-%m-%d')
    
    orders_today = Order.objects.filter(created_at__date=today).count()
    order_counter = orders_today + 1
    
    return f"O-{formatted_date}-{order_counter:04}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    order_id = models.CharField(primary_key=True, max_length=15, default=generate_order_id)
    table_number = models.IntegerField(null=False, blank=False)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order #{self.order_id} - {self.customer_name} - {self.total_amount} - {self.status}"

    def save(self, *args, **kwargs):
        # If object is being updated, calculate the total amount
        if self.pk:
            self.calculate_total_amount()
        super().save(*args, **kwargs)  # Save the instance

    def calculate_total_amount(self):
        # Calculate the total amount from related OrderItems
        total_amount = sum(item.total for item in self.order_items.all())
        self.total_amount = total_amount
        # Save the total amount
        super().save(update_fields=['total_amount'])

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    extra_tip = models.CharField(max_length=250, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.total = self.item.price * self.quantity  # Calculate total for this OrderItem
        super().save(*args, **kwargs)
        # Update the related Order's total_amount after saving OrderItem
        self.order.calculate_total_amount()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        # Update the related Order's total_amount after deleting OrderItem
        self.order.calculate_total_amount()

    def __str__(self):
        return f"{self.order} - {self.item} - {self.quantity}"