from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.core.validators import EmailValidator, RegexValidator

class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    reorder_level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    # def update_quantity(self, qty):
    #     self.quantity += qty
    #     self.save()

    # def is_below_reorder_level(self):
    #     return self.quantity <= self.reorder_level


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, validators=[EmailValidator()], blank=False, null=False)
    phone = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
                             blank=False, null=False)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Expense(models.Model):
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.description} - {self.amount}"



class PurchaseOrder(models.Model):
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='purchase_orders')
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} from {self.supplier.name} on {self.order_date}"

    # def update_total_amount(self):
    #     total = sum(item.quantity * item.price for item in self.order_items.all())
    #     self.total_amount = total
    #     self.save()


class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='order_items')
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.inventory_item.name} for Order {self.purchase_order.id}"


# @receiver(post_save, sender=PurchaseOrderItem)
# def update_inventory_on_order_save(sender, instance, created, **kwargs):
#     if created:
#         instance.inventory_item.update_quantity(instance.quantity)


# @receiver(pre_delete, sender=PurchaseOrderItem)
# def update_inventory_on_order_delete(sender, instance, **kwargs):
#     instance.inventory_item.update_quantity(-instance.quantity)


# @receiver(post_save, sender=PurchaseOrder)
# def update_order_total_amount(sender, instance, created, **kwargs):
#     instance.update_total_amount()
