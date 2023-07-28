import socket
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Employee, Department, Designation
from django.shortcuts import render, redirect
import datetime
import urllib.parse
import random
import smtplib


# Create your views here.


def login_page(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def check_login(request):
    uname=request.POST.get('u_nm')
    password=request.POST.get('pwd')
    user=authenticate(username=uname,password=password)
    if user is not None:
        login(request,user)
        return render(request, 'index.html')
    else:
        param={'msg_danger':'username or password does not match'}
        return render(request, 'login.html', param)

def view_employee(request):
    record=Employee.objects.all()
    param={'data':record}
    return render(request, 'view_employee.html', param)

def add_employee(request):
    return render(request, 'add_employee.html')


def new_emp(request):
    try:
        e_id=request.POST.get('eid')
        first_name=request.POST.get('f_nm')
        last_name=request.POST.get('l_nm')
        dept_name=request.POST.get('dept')
        salary=request.POST.get('sal')
        bonus=request.POST.get('bonus')
        designation=request.POST.get('desg')
        phone=request.POST.get('ph_no')
        DOJ=request.POST.get('DOJ')
        data=Employee(Eid=e_id,First_name=first_name,Last_name=last_name,Dept=dept_name,Salary=salary,Bonus=bonus,Desg=designation,Phone=phone,DOJ=DOJ)
        data.save()
        param={'msg_success':'Employee added successfully'}
        return render(request, 'add_employee.html', param)
    except:
        param={'msg_danger':'an error occured! try to enter different Eid'}
        return render(request, 'add_employee.html', param)

def remove_employee(request):
    record=Employee.objects.all()
    param={'data':record}
    return render(request, 'remove_employee.html', param)

def remove_emp(request):
    e_id=request.GET.get('eid')
    f_name=request.GET.get('f_nm')
    l_name=request.GET.get('l_nm')
    Employee.objects.get(Eid=e_id,First_name=f_name,Last_name=l_name).delete()
    param={'msg_success':'Record deleted'}
    return render(request, 'remove_employee.html', param)

def filter_employee(request):
    return render(request, 'filter_employee.html')

def filter_emp(request):
    # if request.method=='POST':
        eid=request.POST.get('eid')
        name=request.POST.get('name')
        dept=request.POST.get('dept')
        desg=request.POST.get('desg')
        data=Employee.objects.all()
        if eid:
            data=data.filter(Eid__icontains=eid)
        if name:
            data=data.filter(Q(First_name__icontains=name)|Q(Last_name__icontains=name))
        if  dept:
            data=data.filter(Dept__icontains=dept)
        if desg:
            data=data.filter(Desg__icontains=desg)
        param={'data':data}
        return render(request, 'remove_employee.html',param)

def edit_employee(request):
    eid=request.GET.get('eid')
    f_name=request.GET.get('f_nm')
    l_name=request.GET.get('l_nm')
    dept=request.GET.get('dept')
    sal=request.GET.get('sal')
    bonus=request.GET.get('bonus')
    desg=request.GET.get('desg')
    phone=request.GET.get('phone')
    doj=request.GET.get('date_join')
    param={'eid':eid,'f_name':f_name,'l_name':l_name,'dept':dept,'sal':sal,'bonus':bonus,'desg':desg,'phone':phone,'doj':doj}
    return render(request, 'edit_employee.html', param)

def edit_emp(request):
    eid=request.POST.get('e_id')
    first_nm=request.POST.get('first_nm')
    l_name=request.POST.get('last_nm')
    dept=request.POST.get('dept')
    sal=request.POST.get('sal')
    bonus=request.POST.get('bonus')
    desg=request.POST.get('desg')
    phone=request.POST.get('phone')
    doj=request.POST.get('doj')
    data=Employee.objects.get(Eid=eid,First_name=first_nm,Last_name=l_name)
    data.Dept=dept
    data.Salary=sal
    data.Bonus=bonus
    data.Desg=desg
    data.Phone=phone
    data.DOJ=doj
    data.save()
    #param={'msg_success':'data updated'}
    record = Employee.objects.all()
    param = {'data': record,'msg_success':'data updated'}
    return render(request, 'remove_employee.html', param)
    #return redirect('remove_employee')
    # return HttpResponse('<h1>data updated</h1>')
def logout_user(request):
    logout(request)
    param={'msg_success':'Logout successfully!'}
    return render(request,'login.html',param)

def registration(request):
    return render(request, 'registration.html')

def signup(request):
    unm=request.GET.get('unm')
    email=request.GET.get('email')
    pwd=request.GET.get('pwd')
    data=User.objects.create_user(unm,email,pwd)
    data.save()
    param={'msg_success':'Registration successful!'}
    return render(request, 'login.html', param)

def forgot_pass(request):
    return render(request, 'forgot_pass.html')

def forgot_password(request):
    user_nm=request.GET.get('unm')
    email=request.GET.get('email')
    try:
        if socket.create_connection(('8.8.8.8',53), timeout=3):
            # param={'msg_success':'you are connected'}
            # return render(request,'reset_pass.html', param)
            try:
                user=User.objects.get(username=user_nm)
                user_email=user.email
                if email==user_email:
                    server=smtplib.SMTP("smtp.gmail.com",587)
                    server.starttls()
                    server.login("emp.management.2023@gmail.com","wdxzvotqewbchsbm")
                    otp=str(random.randint(1000,9999))
                    msg="your otp for password reset is "+str(otp)
                    server.sendmail("emp.management.2023@gmail.com",user_email,msg)
                    server.quit()
                    param={'msg_success':"OTP sent to your registered email address!",'user_nm':user_nm,'email':email,'otp':otp}
                    return render(request, 'reset_pass.html', param)
                else:
                    param={'msg_danger':'Email address you have entered does not match with registered email!'}
                    return render(request, 'forgot_pass.html', param)

            except User.DoesNotExist:
                param={'msg_danger':"Uer does not exist!"}
                return render(request, 'forgot_pass.html', param)
    except:
        param={'msg_danger':'It seems you are not connected with internet. please check!'}
        return render(request, 'forgot_pass.html', param)
# def reset_pass(request):
#     return render(request, 'reset_pass.html')

def reset_password(request):
    u_otp=request.GET.get('u_otp')
    otp=request.GET.get('otp')
    user=request.GET.get('unm')
    if str(u_otp)==str(otp):
        param={'msg_success':'OTP verified! please enter your new password','usernm':user}
        return render(request, 'new_pass.html', param)
    else:
        param={'msg_danger':'invalid OTP'}
        return render(request, 'forgot_pass.html', param)
    
# def new_pass(request):
#     return render(request, 'new_pass.html')

def new_password(request):
    new_pwd=request.GET.get('new_pwd')
    conf_pwd=request.GET.get('conf_pwd')
    user_nm=request.GET.get('user_nm')

    if new_pwd==conf_pwd:
        user=User.objects.get(username=user_nm)
        user.set_password(new_pwd)
        user.save()
        param={'msg_success':'password changed successfully!'}
        return render(request, 'login.html', param)
    elif new_pwd!=conf_pwd:
        param={'msg_danger':'Password does not match!'}
        return render(request, 'forgot_pass.html', param)