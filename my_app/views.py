from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *

def home(request):
    if request.method == "POST":
        create = task_form(request.POST)
        if create.is_valid():
            create.save()
            return redirect("/my_project/read")

    return render(request,'index.html',{'data': task_form()})

def read(request):
    read_data = guna.objects.all()
    print(read_data)
    return render(request,'read.html',{'data': read_data})

def delete_task(request,id):
    delete_user = guna.objects.get(id = id)
    delete_user.delete()
    return redirect("/my_project/read")
    
def update_task(request,id):
    edit_user = guna.objects.get(id = id)
     
    context = {
        'update_student': task_form(instance=edit_user)
     }
    print(context)
    if request.method == "POST":
        update_task = task_form(request.POST,instance=edit_user)

        if update_task.is_valid():
            update_task.save()
            return redirect("/my_project/read/")

    return render(request,'update.html',context)
# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 != password2:
            messages.error(request,"invalid")
        elif User.objects.filter(username=username).exists():
            messages.error(request,"already exist")
        elif User.objects.filter(email=email):
            messages.error(request,'Your email already exixst')
        else:
            user = User.objects.create_user(username=username,email=email,password=password1)
            user.save()
            messages.success(request,"complete")
            return redirect('login')
    return render(request,'signup.html')

def login_view(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Enter valid username or password")
            
    return render(request,'login.html')
#