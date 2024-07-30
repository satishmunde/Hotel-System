from django.contrib.auth.models import AbstractUser
from django.db import models

def generate_emp_id():
    latest_emp = LoginSystem.objects.order_by('emp_id').last()
    if latest_emp:
        latest_number = int(latest_emp.emp_id[4:]) + 1
    else:
        latest_number = 1

    return f"EMP-{latest_number:07}"


class LoginSystem(AbstractUser):
    id = models.AutoField(primary_key=True)
    emp_id = models.CharField(unique=True, max_length=11,)
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
    access_token = models.TextField(blank=True, null=True)
    refresh_token = models.TextField(blank=True, null=True)
    profile_pictures = models.ImageField(upload_to='profile_pictures/',)
    is_active = models.BooleanField(default=True)
    is_doc_uploaded = models.BooleanField(default=False)
    
    
    
    USERNAME_FIELD = 'emp_id'
    
    
    def generate_emp_id(self):
        latest_emp = LoginSystem.objects.order_by('emp_id').last()
        if latest_emp:
            latest_number = int(latest_emp.emp_id[4:]) + 1
        else:
            latest_number = 1

        return f"EMP-{latest_number:07}"
    
    
    def save(self, *args, **kwargs):
        if not self.emp_id:
            self.emp_id = self.generate_emp_id()
        super().save(*args, **kwargs)


    
    

    def __str__(self):
        return f" {self.emp_id} {self.first_name} {self.last_name} "
    
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
        
        

from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage
from .models import LoginSystem

@receiver(pre_save, sender=LoginSystem)
def delete_old_profile_picture(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).profile_pictures
    except sender.DoesNotExist:
        return False

    new_file = instance.profile_pictures
    if not old_file == new_file:
        if old_file and default_storage.exists(old_file.path):
            default_storage.delete(old_file.path)

@receiver(post_delete, sender=LoginSystem)
def delete_profile_picture_on_delete(sender, instance, **kwargs):
    if instance.profile_pictures and default_storage.exists(instance.profile_pictures.path):
        default_storage.delete(instance.profile_pictures.path)
