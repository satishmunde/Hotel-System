from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



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
        return f"{self.first_name} {self.last_name}"
    
class Document(models.Model):
    employee = models.ForeignKey(Employee, related_name='documents', on_delete=models.CASCADE)
    document_type = models.CharField(max_length=100)
    document = models.FileField(upload_to='employee_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.document_type}"


class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class EmployeePosition(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.SET_DEFAULT ,default=-1)
    department = models.ForeignKey(Department, on_delete=models.SET_DEFAULT ,default=-1)
    position = models.ForeignKey(Position, on_delete=models.SET_DEFAULT ,default=-1)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee} - {self.position}"


class RequiredDocument(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
