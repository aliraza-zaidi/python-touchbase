from django.db import models

# Create your models here.
class Application (models.Model):
    employee_id = models.CharField(max_length=10,default='XYz')
    leave = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10,default='Pending')
