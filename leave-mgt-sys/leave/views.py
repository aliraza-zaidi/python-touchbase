from django.shortcuts import render,redirect
from application.models import Application
from .models import Leave
from .form import LeaveForm
# Create your views here.
def leave (request):
    applications = Application.objects.all()
    return render (request,"Leave.html",{'applications':applications})

def leave_form (request):
    form = LeaveForm()
    return render (request,'leaveform.html',{'form':form})

def submit_form (request):
    if request.method == "POST":
        type = request.POST.get('type')
        descp = request.POST.get('descp')
        date = request.POST.get('date')

        if Leave.objects.filter(type=type).exists():
            error_message = 'Leave Type Already exists.'
            return render (request,'leaveform.html',{'error_message':error_message})

        obj = Leave(type=type,descp=descp,date=date)
        obj.save()
    return render (request,'submitformL.html')

def approve (request, employee_id):
    app = Application.objects.get(employee_id=employee_id)
    app.status = "Approved"
    app.save()
    return redirect('leave')

def decline (request, employee_id):
    app = Application.objects.get(employee_id=employee_id)
    if app.status != 'Approved':
        app.status = "Declined"
        app.save()
    return redirect('leave')