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
    




def generate_emp_id():
    latest_emp = Employee.objects.order_by('emp_id').last()
    if latest_emp:
        latest_number = int(latest_emp.emp_id[3:]) + 1
    else:
        latest_number = 1
    return f"EMP{latest_number:07}"

class Employee(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=10,default=generate_emp_id)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)
   
    address = models.CharField(max_length=255, )
    birth_date = models.DateField()
    
    # Additional fields
    aadhar_number = models.CharField(max_length=20, )
    pan_number = models.CharField(max_length=20, )
    bank_name = models.CharField(max_length=100, )
    bank_account_number = models.CharField(max_length=50, )
    bank_ifsc_code = models.CharField(max_length=20, )
    
    is_doc_uploaded = models.BooleanField(default=False)
    
    

    def __str__(self):
        return f" {self.emp_id} {self.first_name} {self.last_name} "
    
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()
    
class Document(models.Model):
    employee = models.ForeignKey(Employee, related_name='documents', on_delete=models.CASCADE)
    document_type = models.CharField(max_length=100)
    document = models.FileField(upload_to='employee_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
   
    
    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.document_type}"
    
    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()


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
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
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
