from django.shortcuts import render , redirect 
from web.models import obj
from django.http import HttpResponseRedirect
from django.db import models
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import login,logout
from .forms import *
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.




def home(request): 
        
    return render(request, 'webview/home.html')




def signup(request):
    if request.method=='POST':
        form=signupForm(request.POST)
        if form.is_valid():
            firstname=form.cleaned_data['name'] 
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=User.objects.create_user(username, password=password)
            user.first_name=firstname
            user.save()
            login(request, user)
            return redirect('/')
    return render(request,'webview/signup.html')


    

def signin(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('/')
    return render(request, 'webview/signin.html')



def signout(request):
    if request.method=='POST':
        logout(request)
        return redirect('/')

    return render(request, 'webview/logout.html')

##testttt##

@login_required()
def createpost(request):
    if request.method == "POST":
        form = CreateequipmentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('web:equipments')
    else:
        form = CreateequipmentForm()
    return render(request, 'webview/createpost.html', {'form': form})


def equipment_list(request,category= None):
    if category is not None:
        equipments = obj.objects.filter(category=category)
        context = {'equipments' : equipments, 'category': category }
    else:
        equipments = obj.objects.all()
        context = {'equipments' : equipments}
    return render(request, 'webview/equipment_list.html' , context)

def finish_equipment(request, id):
    equipment = obj.objects.get(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def change_status(request,id):
    equipment = obj.objects.get(id=id)
    equipment.is_finished = True
    equipment.is_notifed = True
    equipment.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

