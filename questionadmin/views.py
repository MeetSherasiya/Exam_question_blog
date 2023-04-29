from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import QuestionAdd
from exam.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import superuser_required

# Create your views here.
def login_user(request):
    logout(request)
    try:
        if request.user.is_authenticated:
            return redirect('/admin/dashboard/')

        if request.method == "POST":
            username = request.POST['username']
            userpassword = request.POST['pass']
            myuser = User.objects.filter(username = username)
            if not myuser.exists():
                messages.info(request,"Invalid Credentials")
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
            myuser = authenticate (username = username, password=userpassword)

            if myuser and myuser.is_superuser:
                login(request, myuser)
                if myuser.has_perm('admin.additem'):
                    return redirect('/admin/additem/')
                else:
                    return redirect('/admin/dashboard')

            messages.info(request, 'Invalid password')
            return redirect('/admin/')
    
        return render(request,'login.html')
    
    except Exception as e:
        print(e)

@login_required(login_url='/admin/')
def index(request):
    table = Paper.objects.all()
    return render(request, 'admin.html', {'table': table})

@login_required(login_url='/admin/')
def Additem(request):
    form = QuestionAdd()
    if request.method == "POST":
        form = QuestionAdd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data added successfully.')
            return redirect('/admin/additem/')
    return render(request, 'addadmin.html', {'form': form})

@login_required(login_url='/admin/')
def delete(request, id):
    if request.method == "POST":
        student = Paper.objects.get(id=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))

@login_required(login_url='/admin/')
def edit(request, id):
    if request.method == "POST":
        question = Paper.objects.get(pk=id)
        form = QuestionAdd(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    else:
        question = Paper.objects.get(pk=id)
        form = QuestionAdd(instance=question)
    return render(request, 'edit.html',{'form': form})

def logout_user(request):
    logout(request)
    return redirect('/admin/')