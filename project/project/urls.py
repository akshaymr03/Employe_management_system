"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from tkinter import N
from django.contrib import admin
from django.urls import re_path,include
from django.core.checks.messages import DEBUG
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^index$',views.index,name='index'),
    re_path(r'^signup/$',views.signup,name='signup'),
    re_path(r'^$',views.login,name="login"),
    #re_path(r'accounts/',include('django.contrib.auth.urls')),
    re_path(r'^registration$',views.registration,name='registration'),
    re_path(r'^display$',views.display,name='display'),
    re_path(r'^view(?P<pk>\d+)/$',views.view,name='view'),
    re_path(r'^edit(?P<pk>\d+)/$',views.edit,name='edit'),
    re_path(r'^delete(?P<pk>\d+)/$',views.delete,name='delete'),
    re_path(r'^employee_delete(?P<pk>\d+)/$',views.employee_delete,name='employee_delete'),
    re_path(r'^user_delete(?P<pk>\d+)/$',views.user_delete,name='user_delete'),
    re_path(r'^attendances$',views.attendances,name='attendances'),
    re_path(r'^attendance_display$',views.attendance_display,name='attendance_display'),
    re_path(r'^user$',views.user,name='user'),
    re_path(r'logout/$', views.user_logout, name="logout"),
    re_path(r'^employee_signup/$',views.employee_signup,name='employee_signup'),
    re_path(r'^ex_employee/$',views.ex_employee,name='ex_employee'),
    re_path(r'^error/$',views.error,name='error'),
    re_path(r'^employee_display/$',views.employee_display,name='employee_display'),
    re_path(r'^employee_home/$',views.employee_home,name='employee_home'),
    re_path(r'^user_logout/$',views.user_logout,name='user_logout'),
    re_path(r'^profile/$',views.profile,name='profile'),
    re_path(r'^message/$',views.message,name='message'),
    re_path(r'^send_message/$',views.send_message,name='send_message'),
    re_path(r'^inbox/$',views.inbox,name='inbox'),
    re_path(r'^user_attendance/$',views.user_attendance,name='user_attendance'),
    re_path(r'^search/$',views.search,name='search'),
]

if(settings.DEBUG):
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)