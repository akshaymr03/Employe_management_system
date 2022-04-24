from array import array
from email import message
from platform import uname
from pyexpat.errors import messages
from unicodedata import name
from django.shortcuts import redirect, render
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myapp.forms import *
from myapp.models import *
from django.http import HttpResponse
import datetime
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

def employee_home(request):
    if 'username' in request.session:
        a=request.session['username']
        '''b=admin.objects.get(name=a)
        c=b.email
        d=admin.objects.filter(name=a)
        print(d.email)
        x=datetime.datetime.now()
        c={'d':b,'x':x}'''
        return render(request,'employee_home.html')
    else:
        return redirect(login)
    

def profile(request):
    if 'username' in request.session:
        a=request.session['username']
        b=admin.objects.get(username=a)
        c=b.emp_id 
        form=employee.objects.get(emp_id=c)
        return render(request,'profile.html',{'form':form})
    else:
        return redirect(employee_home)


def signup(request):
    if request.method=="POST":
        forms=admin_registration(request.POST)
        if forms.is_valid():
            f=forms.save(commit=False)
            f.is_admin=True
            f.save()
            return index(request)
        else:
            return error(request)
    return render(request,'signup.html')

def employee_signup(request):
    #d=employee.objects.get(pk=pk)
    #form=admin_registration()
    if request.method=="POST":
        form=admin_registration(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.is_employee=True
            f.save()
            return index(request)
        else:
            return error(request)
    return render(request,'employee_signup.html')


def login(request):
    if 'username' in request.session:
        return redirect(employee_home)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(username=username, password=password)
        
        if user and user.is_admin == True:
            login_required(request,user)
            return index(request)
        elif user and user.is_employee == True:
            login_required(request,user)
            request.session['username'] = username
            return redirect (employee_home)
        else:
            return HttpResponse("Invalid login details.....")

    return render(request, 'login.html')

def user_logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect(login)

def registration(request):
    form=employee_registration()
    if request.method=='POST':
        src=request.POST['emp_id']
        print(src)
        form=employee_registration(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'employee_signup.html',{'src':src})
        else:
            print("ERROR FROM INVALID")
    return render(request,'registration_employee.html')


def display(request):
    d=employee.objects.filter(status='active')
    return render(request,'display.html',{'view':d})

def ex_employee(request):
    d=employee.objects.filter(status='inactive')
    return render(request,'display.html',{'view':d})

def view(request,pk):
    d=employee.objects.get(pk=pk)
    return render (request,'view.html',{'form':d})


def edit(request,pk):
    x=employee.objects.get(pk=pk)
    form=employee_registration(instance=x)
    if request.method=='POST':
        forms=employee_registration(request.POST,request.FILES,instance=x)
        if forms.is_valid():
            forms.save()
            return display(request)
        else:
            return error(request)
    return render(request,'edit.html',{'form':form})


def delete(request,pk):
    d=messages.objects.get(pk=pk)
    d.delete()
    return send_message(request)
      
def employee_delete(request,pk):
    d=employee.objects.get(pk=pk)
    d.delete()
    return display(request)


def attendances(request):
    if 'username' in request.session:
        a=request.session['username']
        if request.method=='POST':
            forms=Attendanceform(request.POST)
            if forms.is_valid():
                forms.save()
                return employee_home(request)
            else:
                print("ERROR")
        b=admin.objects.get(username=a)
        c=b.emp_id 
        d=employee.objects.get(emp_id=c)
        x=datetime.datetime.now()
        c={'d':d,'x':x}
    return render(request,'attendance.html',{'c':c})


'''def attendance_display(request):
    d=attendance.objects.all()
    return render(request,'attendance_display.html',{'form':d})'''


def user(request):
    d=admin.objects.all()
    return render(request,'admin.html',{'view':d})


def user_delete(request,pk):
    d=admin.objects.get(pk=pk)
    d.delete()
    return user(request)

def error(request):
    return render(request,'error.html')

def employee_display(request,id):
    d=employee.objects.filter(id=id)
    return render(request,'display.html',{'view':d})


def message(request):
    if 'username' in request.session:
        a=request.session['username']
        if request.method=='POST':
            forms=message_form(request.POST)
            if forms.is_valid():
                forms.save()
                return employee_home(request)
            else:
                print("ERROR")
        b=admin.objects.get(username=a)
        c=b.emp_id 
        d=employee.objects.get(emp_id=c)
        x=datetime.datetime.now()
        c={'d':d,'x':x}
    return render(request,'message.html',{'c':c})
    

def send_message(request):
    if 'username' in request.session:
        a=request.session['username']
        b=admin.objects.get(username=a)
        c=b.emp_id 
        f=user_message.objects.filter(emp_id=c)
        return render(request,'send_message.html',{'form':f})
    else:
        return redirect(employee_home)

def inbox(request):
    d=user_message.objects.all()
    return render(request,'inbox.html',{'form':d})

def user_attendance(request):
    if 'username' in request.session:
        a=request.session['username']
        b=admin.objects.get(username=a)
        c=b.emp_id 
        f=attendance.objects.filter(emp_id=c)
        return render(request,'user_attendance.html',{'form':f})
    else:
        return employee_home(request)

def search(request):
    if request.method=='POST':
        src=request.POST['search']
        if src:
            match=employee.objects.filter(Q(name__icontains=src) | Q(emp_id__icontains=src))
            if match:
                return render(request,'search.html',{'srh':match})
            else:
                messages.error(request,"NO RESULT FOUND")
        else:
            messages.error(request,"NO RESULT FOUND")
    return render(request,'search.html')

def attendance_display(request):
    if request.method=='POST':
        src=request.POST['search']
        if src:
            match=attendance.objects.filter(Q(name__icontains=src) | Q(emp_id__icontains=src))
            if match:
                return render(request,'attendance_display.html',{'srh':match})
            else:
                messages.error(request,"NO RESULT FOUND")
        else:
            messages.error(request,"NO RESULT FOUND")
    d=attendance.objects.all()
    return render(request,'attendance_display.html',{'form':d})