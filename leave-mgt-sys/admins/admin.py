from django.contrib import admin
from .models import Admin

class AdminAdmin (admin.ModelAdmin):
    list_display = ['id','name','user_name','email','password','date']

admin.site.register(Admin,AdminAdmin)