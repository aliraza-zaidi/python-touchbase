from django.contrib import admin
from .models import Department

class DepartmentAdmin (admin.ModelAdmin):
    list_display = ('name','short_name','department_id','date')

admin.site.register(Department,DepartmentAdmin)

