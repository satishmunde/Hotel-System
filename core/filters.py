# filters.py
import django_filters
from .models import LoginSystem

class LoginSystemFilter(django_filters.FilterSet):
    class Meta:
        model = LoginSystem
        fields = '__all__'  
        # fields = ['emp_id']
        
