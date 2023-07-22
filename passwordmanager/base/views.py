from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm,PasswordEntryForm
from django.contrib import messages
from .models import User,PasswordEntry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django_otp.decorators import otp_required



def registerPage(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account created successfully'+user)
            return redirect('login')
        else:
            messages.error(request,'Account creation failed')
    context={'form':form}
    return render(request,'base/register.html',context)

def loginPage(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('home',pk=user.id)
        else:
            messages.info(request,'Username or password is incorrect')
                      
    context={}       
    return render(request,'base/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')
    
       
def welcome(request):
    return render(request,'base/welcome.html')

@login_required(login_url='login')
def home(request, pk):
    user = User.objects.get(id=pk)
    form = PasswordEntryForm(request.POST or None)
    q=request.GET.get('q') if request.GET.get('q') != None else ''

    if request.method == 'POST' and form.is_valid():
        password_data = form.save(commit=False)
        password_data.user = user
        password_data.save()
        return redirect('home', pk=user.id)

    passwords = PasswordEntry.objects.filter(user=user)
    search=PasswordEntry.objects.filter(website__icontains=q)
    
    context = {'user': user, 'form': form, 'passwords': passwords,'search':search}
    current_user = request.user

    if current_user == user:
        return render(request, 'base/home.html', context)
    else:
        return HttpResponse('You are not allowed to view this page')
    
    
@login_required(login_url='login')
def password_display(request):
    passwords=PasswordEntry.objects.all()
    context={'password':passwords}
    return render(request,'base/password_display.html',context)


@login_required(login_url='login')  
@otp_required     
def password_info(request,pk):
    password=PasswordEntry.objects.get(id=pk)
    context={'password':password}
    return render(request,'base/password_info.html',context)

@login_required(login_url='login')
def delete_password(request,pk):
    password=PasswordEntry.objects.get(id=pk)
    if request.method=='POST':
        password.delete()
        return redirect('home',pk=request.user.id)
    context={'password':password}
    return render(request,'base/delete_password.html',context)

@login_required(login_url='login')
def delete_profile(request,pk):
    user=User.objects.get(id=pk)
    if request.method=='POST':
        user.delete()
        return redirect('login')
    context={'user':user}
    return render(request,'base/delete_profile.html',context)

    
    





