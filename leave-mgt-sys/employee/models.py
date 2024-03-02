from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Employee (models.Model):
    name = models.CharField(max_length=50)
    employee_id = models.CharField(max_length=15,primary_key=True,unique=True)
    department_id = models.CharField(max_length=5)
    joining_date = models.DateField()
    status = models.CharField(max_length=10,default='Active')
    user_name = models.CharField(max_length=15)
    password = models.CharField(max_length=18)