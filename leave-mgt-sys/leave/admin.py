from django.contrib import admin
from .models import Leave
# Register your models here.
class LeaveAdmin (admin.ModelAdmin):
    list_display = ('type','descp','date')


# Register your models here.
admin.site.register(Leave,LeaveAdmin)