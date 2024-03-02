from django.shortcuts import render
from .form import AdminForm
from .models import Admin
# Create your views here.
def add_admin (request):
    admins = Admin.objects.all()
    return render (request,"Admin.html",{'admins':admins})

def create_admin (request):
    form = AdminForm()
    return render(request,"adminform.html",{'form':form})

def submit_form (request):
    if request.method == "POST":
        name = request.POST.get('name')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        date = request.POST.get('date')

        if Admin.objects.filter(email=email).exists():
            error_message = 'Admin Already exists.'
            return render (request,'leaveform.html',{'error_message':error_message})

        obj = Admin(name=name,user_name=user_name,email=email,password=password,date=date)
        obj.save()
    return render (request,"submitformA.html")