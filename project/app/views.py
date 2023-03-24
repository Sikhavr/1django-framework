from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def hello(request):
    return HttpResponse("helloo")
def temp(request):
    return render(request,"temp.html")
def value(request):
    name='sikha'
    age=2
    return render(request,"value.html",{'data':name,'name':age})
def student1(request):
    data=student.objects.all()
    return render(request,"table1.html",{'name':data})
def studentreg(request):
    return render(request,"studentform.html")
def stud(request):
    n=request.POST["name"]
    a=request.POST["age"]
    data=student(name=n,age=a)
    data.save()
    return HttpResponse("data stored")
def regform(request):
    return render(request,"register.html")
def reg(request):
    n=request.POST["name"]
    a=request.POST["age"]
    e=request.POST["email"]
    p=request.POST["password"]
    c=request.POST["contactnumber"]
    data = registration(name=n,age=a,email=e,password=p,contactnumber=c)
    data.save()
    return HttpResponse("data stored")

def logfun(request):
    a=registration.objects.all()
    b = request.POST["name"]
    c = request.POST["email"]
    key = 0
    for i in a:
        if b == i.name:
            key = 1
            return HttpResponse("login successfull")
    if key == 0:
        return HttpResponse("wrong credentials")
def logfun1(request):
    return render(request,"reglogin.html")
def employeeform2(request):
    form=employeeform()
    if request.method=="POST":
        form=employeeform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("successfull")
    return render(request,"relogin.html",{'form':form})
def studentformpage2(request):
    if request.method=="POST":
        form=studentform2(request.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            age=form.cleaned_data["age"]
            data=student(name=name,age=age)
            data.save()
            return HttpResponse("data stored")
        else:
            return HttpResponse("error")
    return render(request,"studentpage.html")
def fileuploadpage(request):
    if request.method=="POST":
        form=fileuploadform(request.POST,request.FILES)
        if form.is_valid():
            n=form.cleaned_data["name"]
            f=form.cleaned_data["file"]
            data=fileupload(name=n,file=f)
            data.save()
            return HttpResponse("file uploaded")
        else:
            return HttpResponse("error")
    return render(request,"fileuploadpage.html")















