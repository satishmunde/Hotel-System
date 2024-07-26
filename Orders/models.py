from django.conf import settings
from django.utils import timezone
from django.db import models
from crm.models import Customer
from Menu.models import MenuItem  # Assuming Item model is defined in menu app

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
    
    order_id = models.CharField(primary_key=True, max_length=15,default=generate_order_id)
    table_number = models.IntegerField(null=False ,blank=False)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    employee =  models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order #{self.order_id} - {self.customer_name} - {self.total_amount} - {self.status}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the instance first to get a valid PK
        self.calculate_total_amount()
        super().save(*args, **kwargs)  # Save again after updating total_amount

    def calculate_total_amount(self):
        order_items = self.order_items.all()
        total_amount = sum(item.total for item in order_items)
        self.total_amount = total_amount

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
    extra_tip =  models.CharField(max_length=250, null=True,blank=True )
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.total = self.item.price * self.quantity  # Calculate total for this OrderItem
        super().save(*args, **kwargs)
        self.order.calculate_total_amount()  # Update Order's total_amount after saving OrderItem

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.order.calculate_total_amount()  # Update Order's total_amount after deleting OrderItem

    def __str__(self):
        return f"{self.order} - {self.item} - {self.quantity}"
