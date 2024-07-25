from django.db import models
from django.utils import timezone
from Orders.models import Order




def generate_token_id():
    today = timezone.localdate()
    formatted_date = today.strftime('%y-%m-%d')
    
    orders_today = Token.objects.filter(created_at__date=today).count()
    order_counter = orders_today + 1
    
    return f"T-{formatted_date}-{order_counter:04}"

    
class Token(models.Model):
    token_number = models.CharField(primary_key=True, max_length=15,default=generate_token_id)
    order = models.OneToOneField(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='token')
    is_complated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.token} -  {self.order} - {self.is_complated}"
    
    def delete(self, *args, **kwargs):
        self.is_complated = True
        self.save()
