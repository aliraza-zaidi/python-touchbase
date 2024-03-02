"""
URL configuration for leave_mgt_sys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from admins import views as aViews
from dashboard import views as dViews
from employee import views as eViews
from department import views as dptViews
from leave import views as lViews
from login import views as login
from application import views as application
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login.e_login,name="e_login"),
    path('login/verifying',login.verify,name="verify"),
    path('login/admin-login/',login.a_login,name="a_login"),
    path('application/',application.leave,name="application"),
    path('application/submit-application/',application.submit,name="submitapplication"),
    path('admins/', aViews.add_admin,name="admins"),
    path('admins/adminform', aViews.create_admin,name="adminform"),
    path('admins/adminform/submitform', aViews.submit_form,name="submitformA"),
    path('dashboard/', dViews.dashboard,name='dashboard'),
    path('employee/', eViews.employee,name='employee'),
    path('employee/employee_form/', eViews.employee_form,name='employee_form'),
    path('employee/employee_form/submitform', eViews.submit_form,name='submitform'),
    path('employee/edit-employee/<slug:employee_id>/', eViews.edit_employee,name='edit_employee'),
    path('department/', dptViews.department,name='department'),
    path('department/departmentform', dptViews.department_form,name='department_form'),
    path('department/departmentform/submitform', dptViews.submit_form,name='submitformD'),
    path('leave/', lViews.leave,name='leave'),
    path('leave/approve/<slug:employee_id>/',lViews.approve,name="approve"),
    path('leave/decline/<slug:employee_id>/',lViews.decline,name="decline"),
    path('leave/leaveform/', lViews.leave_form,name='leave_form'),
    path('leave/leaveform/submitform', lViews.submit_form,name='submitformL'),
    path('employee/delete-employee/<slug:employee_id>/', eViews.delete_employee, name='delete_employee'),
]
