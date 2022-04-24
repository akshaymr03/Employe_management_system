from pyexpat import model
from random import choices
from django.db.models import fields
from django.forms import widgets
from django import forms
from myapp.models import admin, employee,attendance, user_message
from django.contrib.auth.forms import UserCreationForm

class admin_registration(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=admin
        fields=UserCreationForm.Meta.fields +('emp_id','first_name','last_name','age','email','addres','number')
        widgets={
            
        }

class employee_registration(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'
        widgets={
            'gender':forms.RadioSelect(),
            'status':forms.Select(),
            'dob':forms.NumberInput(attrs={'type':'date'}),
            'date_of_join':forms.NumberInput(attrs={'type':'date'})
        }
        

class Attendanceform(forms.ModelForm):
    class Meta:
        model = attendance
        fields = '__all__'
        widgets = {
            'attendances':forms.Select()
        }

class message_form(forms.ModelForm):
    class Meta:
        model=user_message
        fields='__all__'
        widgets={
            
        }