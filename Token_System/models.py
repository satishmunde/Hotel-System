from django.db import models

from Orders.models import Order

class Token(models.Model):
    token_number = models.CharField(max_length=50, unique=True)
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='token')
    is_complated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.token} -  {self.order} - {self.is_complated}"
    
    def delete(self, *args, **kwargs):
        self.is_complated = True
        self.save()
