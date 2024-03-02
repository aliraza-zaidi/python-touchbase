from django.db import models

# Create your models here.
class Leave (models.Model):
    type = models.CharField(max_length=20)
    descp = models.TextField(max_length=200)
    date = models.DateField(auto_now_add=True)