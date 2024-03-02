from django.db import models

# Create your models here.
class Department (models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=5)
    department_id = models.CharField(max_length=5,primary_key=True,unique=True)
    date = models.DateField(auto_now_add=True)