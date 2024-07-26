from django.contrib.auth.models import AbstractUser
from django.db import models

def generate_emp_id():
    latest_emp = LoginSystem.objects.order_by('emp_id').last()
    if latest_emp:
        latest_number = int(latest_emp.emp_id[3:]) + 1
    else:
        latest_number = 1
    return f"EMP-{latest_number:07}"


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, emp_id, password=None, **extra_fields):
        if not emp_id:
            raise ValueError('The Employee ID field must be set')
        user = self.model(emp_id=emp_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, emp_id, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(emp_id, password, **extra_fields)

class LoginSystem(AbstractUser):
    emp_id = models.CharField(primary_key=True, max_length=11, default=generate_emp_id)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=255,)
    aadhar_number = models.CharField(max_length=20,)
    pan_number = models.CharField(max_length=20,)
    bank_name = models.CharField(max_length=100,)
    bank_account_number = models.CharField(max_length=50,)
    bank_ifsc_code = models.CharField(max_length=20,)
    profile_pictures = models.ImageField(upload_to='profile_pictures/',)
    is_active = models.BooleanField(default=True)
    is_doc_uploaded = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    
    USERNAME_FIELD = 'emp_id'


    
    

    def __str__(self):
        return f" {self.emp_id} {self.first_name} {self.last_name} "
    
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
