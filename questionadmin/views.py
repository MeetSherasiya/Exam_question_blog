from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import QuestionAdd
from exam.models import *
from django.contrib import messages

# Create your views here.
def index(request):
    table = Paper.objects.all()
    return render(request, 'admin.html', {'table': table})

def Additem(request):
    form = QuestionAdd()
    if request.method == "POST":
        form = QuestionAdd(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data added successfully.')
            return redirect('/admin/additem/')
    return render(request, 'addadmin.html', {'form': form})

def delete(request, id):
    if request.method == "POST":
        student = Paper.objects.get(id=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))

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