from django.db import models
from django import forms

class Admin (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    date = models.DateField(auto_now_add=True)