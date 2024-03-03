from django.shortcuts import render,redirect
from admins.models import Admin
from employee.models import Employee
def get_employee_id (username):
    user = Employee.objects.get(user_name=username)
    return user.employee_id

def verify (request):
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        print(user_name,password)
        employee_id = get_employee_id(username=user_name)
        print(employee_id)
        if Employee.objects.filter(user_name=user_name,password=password).exists():
            return render (request,'EmployeeApplication.html',{'employee_id':employee_id})
        return redirect('e_login')
def e_login (request):
    return render(request, 'Employeelogin.html')

def a_login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if Admin.objects.filter(user_name=username,password=password).exists():
            return render(request,'Dashboard.html')
        else:
            return render(request, 'AdminLogin.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'AdminLogin.html')