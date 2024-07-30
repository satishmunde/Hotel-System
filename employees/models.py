from django.conf import settings
from django.db import models


def generate_dept_id():
    latest_dept = Department.objects.order_by('dept_id').last()
    if latest_dept:
        latest_number = int(latest_dept.dept_id[5:]) + 1
    else:
        latest_number = 1
    return f"DEPT-{latest_number:05}"

class Department(models.Model):
    dept_id = models.CharField(primary_key=True, max_length=10,default=generate_dept_id)
    name = models.CharField(max_length=100, null=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f" {self.dept_id} {self.name} "
    
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
    

    
class Document(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='documents', on_delete=models.CASCADE)
    document_type = models.CharField(max_length=100)
    document = models.FileField(upload_to='employee_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
   
    
    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.document_type}"
    
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
        
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django.core.files.storage import default_storage
from .models import Document

@receiver(pre_save, sender=Document)
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

@receiver(post_delete, sender=Document)
def delete_profile_picture_on_delete(sender, instance, **kwargs):
    if instance.profile_pictures and default_storage.exists(instance.profile_pictures.path):
        default_storage.delete(instance.profile_pictures.path)



def generate_pos_id():
    latest_pos = Position.objects.order_by('pos_id').last()
    if latest_pos:
        latest_number = int(latest_pos.pos_id[4:]) + 1
    else:
        latest_number = 1
    return f"POS-{latest_number:04}"

class Position(models.Model):
    
    pos_id = models.CharField(primary_key=True, max_length=8,default=generate_pos_id)
    name = models.CharField(max_length=100 ,null=False)
    is_active = models.BooleanField(default=True)
   

    def __str__(self):
        return f" {self.pos_id} {self.name} "
    
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

class EmployeePosition(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        # {self.employee__first_name} - {self.employee__last_name} -
        return f"{self.employee} -  {self.position} - {self.department}"
    
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()

    def save(self, *args, **kwargs):
        if self.employee_id is None or self.department_id is None or self.position_id is None:
            raise ValueError("Employee, department, and position must be specified.")
        super().save(*args, **kwargs)

class RequiredDocument(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()


class EmployeePayment(models.Model):
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)  # e.g., Bank Transfer, Cash
    description = models.CharField(max_length=255)  # e.g., Salary, Bonus
    document = models.FileField(upload_to='employee_payment_slip/')

    def __str__(self):
        return f"Payment of {self.amount} to {self.employee.first_name} {self.employee.last_name} on {self.payment_date}"