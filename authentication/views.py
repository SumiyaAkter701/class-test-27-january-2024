
from django.shortcuts import render,redirect,HttpResponse
from .form import SignUp_From, SignIn_Form,Profile_Form
from django.contrib.auth import authenticate,login,logout
from .models import CustomUser
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def sign_up(request):
    form = SignUp_From()
    if request.user.is_authenticated:
        return redirect('sign_in')
    if request.method == 'POST':
        form  = SignUp_From(request.POST)
        if form.is_valid():
            user = form .save() 
            password = form .cleaned_data['password1']
            user.set_password(password)
            user.save()
            return redirect('sign_in')
        else:
            return HttpResponse(form.errors)
        
    return render(request,'sign_up.html',{'form':form})

def sign_in(request):
    if request.method=="POST":
        form=SignIn_Form(request.POST)
        if form.is_valid():
            
            email=form.cleaned_data.get('email')
            custom_user = CustomUser.objects.get(email=email)
            username = custom_user.username
            password=form.cleaned_data.get('password')
            
            user = authenticate(request, username=username, password=password)
            print(user)
            if not user:
                messages.warning(request,'The User Account not found')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            if user:
                
                login(request, user)
                return redirect("home")
    else:
        form=SignIn_Form()
    
    return render(request,'sign_in.html',{'form':form})

def sign_out(request):
    logout(request)
    return redirect('sign_in')

def home(request):
    form= Profile_Form()
    if request.method=='POST':
        form=Profile_Form(request.POST)
        if form.is_valid():
            user= form.save()
            user.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    return render(request,'home.html', {'form':form})

def profile(request):
    
    return render(request,'profile.html')






