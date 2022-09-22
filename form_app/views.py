from django.shortcuts import render,redirect
from django.views import View
from .models import Mari

# Create your views here.

def home(request):
    mydata=Mari.objects.all()
    if(mydata!=''):
        return render(request,'index.html',{'datas':mydata})
    else:
        return render(request,'index.html')

def addData(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        aadhar=request.POST['aadhar']
        dept=request.POST['dept']

        obj=Mari()
        obj.Name=name
        obj.Email=email
        obj.Aadhar=aadhar
        obj.Department=dept
        obj.save()
        mydata=Mari.objects.all()
        return redirect('home')
    return render(request,'index.html')

def updateData(request,id):
    mydata=Mari.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        aadhar=request.POST['aadhar']
        dept=request.POST['dept']

        mydata.Name=name
        mydata.Email=email
        mydata.Aadhar=aadhar
        mydata.Department=dept
        mydata.save()
        return redirect('home')
    return render(request,'edit.html',{'data':mydata})

def deleteData(request,id):
    mydata=Mari.objects.get(id=id)
    mydata.delete()
    return redirect('home')

