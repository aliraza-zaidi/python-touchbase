from django.shortcuts import render
from .models import Department
from .form import DepartmentForm
# Create your views here.
def department (request):
    departments = Department.objects.all()
    return render (request,"Department.html",{'departments':departments})

def department_form (request):
    form = DepartmentForm()
    return render(request,"departmentform.html",{'form':form})

def submit_form (request):
    if request.method == "POST":
        name = request.POST.get('name')
        short_name = request.POST.get('short_name')
        department_id = request.POST.get('department_id')
        date = request.POST.get('date')

        if Department.objects.filter(department_id=department_id).exists():
            error_message = f'Department with department id {department_id} already exists.'
            return render (request,'departmentform.html',{'error_message':error_message})
        obj = Department(name=name,short_name=short_name,department_id=department_id,date=date)
        obj.save()
    return render(request,"submitformD.html")