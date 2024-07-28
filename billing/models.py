from django.db import models
from orders.models import Order
from django.utils import timezone
from crm.models import Customer

class Bill(models.Model):
    bill_id = models.CharField(primary_key=True, max_length=18, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer_id =models.ForeignKey(Customer, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def generate_bill_id(self):
        today = timezone.localdate()
        formatted_date = today.strftime('%y-%m-%d')
        bills_today = Bill.objects.filter(created_at__date=today).count()
        bill_counter = bills_today + 1
        return f"Bill-{formatted_date}-{bill_counter:04}"

    def save(self, *args, **kwargs):
        if not self.bill_id:
            self.bill_id = self.generate_bill_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.bill_id


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('upi', 'UPI'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
    ]

    payment_id = models.CharField(primary_key=True, max_length=13, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cash')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)


    def generate_payment_id(self):
        today = timezone.localdate()
        formatted_date = today.strftime('%y-%m-%d')
        payments_today = Payment.objects.filter(payment_date__date=today).count()
        payment_counter = payments_today + 1
        return f"{formatted_date}-{payment_counter:04}"

    def save(self, *args, **kwargs):
        if not self.payment_id:
            self.payment_id = self.generate_payment_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.payment_id
