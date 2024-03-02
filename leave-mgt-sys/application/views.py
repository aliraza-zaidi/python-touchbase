from django.shortcuts import render
from .models import Application
from leave.models import Leave
# Create your views here.
def leave (request):
    leave_types = Leave.objects.values_list('type', flat=True).distinct()
    print(leave_types)
    return render (request, "EmployeeApplication.html",leave_types)

def submit (request):
    leave_types = Leave.objects.values_list('type', flat=True).distinct()
    print(leave_types)
    if request.method == "POST":
        employee_id = request.POST.get('employee_id')
        leave = request.POST.get('Leave')
        print(leave,employee_id)

        obj = Application(employee_id=employee_id,leave=leave)
        obj.save()

        return render (request,'submitapplication.html',leave_types)