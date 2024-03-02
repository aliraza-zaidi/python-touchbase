from django.shortcuts import render,redirect
from .models import Employee
from department.models import Department
from .form import EmployeeForm

def employee (request):
    employees = Employee.objects.all()
    return render(request,"Employee.html",{'employees':employees})

def employee_form (request):
    form = EmployeeForm()
    return render(request,"employeeForm.html",{'form':form})

def submit_form (request):
    if request.method == "POST":
        name = request.POST.get('name')
        employee_id = request.POST.get('employee_id')
        department_id = request.POST.get('department_id')
        joining_date = request.POST.get('joining_date')
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        if Employee.objects.filter(employee_id=employee_id).exists():
            error_message = "An employee with this ID already exists."
            return render (request, 'employeeForm.html', {'error_message':error_message})
        if not Department.objects.filter(department_id=department_id).exists():
            error_message = "No Department exists for this Department ID."
            return render (request, 'employeeForm.html', {'error_message':error_message})
        obj = Employee(name=name,employee_id=employee_id,department_id=department_id,joining_date=joining_date,user_name=user_name,password=password)
        obj.save()
    return render(request,"submitform.html")
def edit_employee (request, employee_id):
    employee = Employee.objects.get(employee_id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect ('employee')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form})

def delete_employee (request,employee_id):
    employee = Employee.objects.get(employee_id=employee_id)
    employee.status = "Inactive"
    employee.save()
    return redirect('employee')
    