from django.shortcuts import render
from django.http import HttpResponse
from employee.models import Employee
from department.models import Department
from leave.models import Leave
from application.models import Application
# Create your views here.
def dashboard (request):
    count_e = Employee.objects.count()
    count_d = Department.objects.count()
    count_l = Leave.objects.count()
    count_approved = Application.objects.filter(status='Approved').count()
    count_declined = Application.objects.filter(status='Declined').count()
    count_pending = Application.objects.filter(status='Pending').count()

    count =  {
        'count_e':count_e,
        'count_d':count_d,
        'count_l':count_l,
        'count_pending':count_pending,
        'count_approved':count_approved,
        'count_declined':count_declined
    }
    
    return (render(request,"Dashboard.html",count))