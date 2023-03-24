"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello),
    path('temp',views.temp,name='temp'),
    # path('staticcss',views.staticcss,name='hii'),
    # path('staticjs',views.staticjs,name='hee'),
    # path('staticimg',views.staticimg,name='hoo'),
    # path('first',views.first,name='first'),
    # path('second',views.second,name='second'),
    # path('navigation',views.navbar,name='navigation'),
    # path('loginpage',views.loginpage,name='loginpage'),
    path('firsttable',views.student1,name='table1'),
    path('studentreg',views.studentreg,name='studentreg'),
    path('stud',views.stud,name='stud'),
    path('regform',views.regform,name='regform'),
    path('reg',views.reg,name='reg'),
    path('logfun',views.logfun,name='logfun'),
    path('reglog',views.logfun1,name='reglog'),
    path('relogin',views.employeeform2,name='employeeform2'),
    path('studentpage',views.studentformpage2,name='studentformpage2'),
    path('filepage',views.fileuploadform,name='fileuploadpage'),
]

