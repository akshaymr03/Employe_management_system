from distutils.command.upload import upload
import email
import numbers
import datetime
from operator import mod
from random import choices
from tkinter import Widget
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class admin(AbstractUser):
    emp_id=models.CharField(max_length=500,unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField(max_length=500,unique=True)
    addres=models.CharField(max_length=250)
    number=models.IntegerField()

    is_admin = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)



class employee(models.Model):
    Choice_value = [('MALE','0'), ('FEMALE', '1')]
    Choice_status = [('active','0'), ('inactive', '1')]
    name=models.CharField(max_length=500)
    dob=models.DateField()
    email=models.EmailField(max_length=500,unique=True)
    gender= models.CharField(max_length=10,choices=Choice_value)
    addres=models.CharField(max_length=500)
    numbers=models.IntegerField()  
    photo=models.ImageField(upload_to='project/photo/')
    degree=models.CharField(max_length=500)
    institution=models.CharField(max_length=500)
    acnumber=models.CharField(max_length=500)
    branch=models.CharField(max_length=500)
    ifsc=models.CharField(max_length=500)
    emp_id=models.CharField(max_length=500,unique=True)
    depaetment=models.CharField(max_length=500)
    date_of_join=models.DateField()
    position=models.CharField(max_length=500)
    salary=models.CharField(max_length=500)
    status=models.CharField(max_length=50,choices=Choice_status)
    cv=models.FileField(upload_to='project/cv/')
    bound=models.FileField(upload_to='project/bound/')
    experience=models.CharField(max_length=500,default='NONE',editable=False)
    company_name=models.CharField(max_length=500,default='NONE',editable=False)
    certificate=models.FileField(upload_to='project/certificate/',default='NONE',editable=False)


class attendance(models.Model):
    attendance_choices = (
    ('present', 'Present'),
    ('absent', 'Absent'), 
    )
    date=models.CharField(max_length=500)
    emp_id=models.CharField(max_length=500)
    name=models.CharField(max_length=500)
    attendances = models.CharField(max_length=8, choices=attendance_choices, blank=True)


class user_message(models.Model):
    date=models.CharField(max_length=500)
    emp_id=models.CharField(max_length=500)
    name=models.CharField(max_length=500)
    msg=models.CharField(max_length=1000)