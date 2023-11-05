from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
# import EmailBckend.py from app
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate,logout,login
def BASE(request):
    return render(request,'base.html')
def LOGIN(request):
    return render(request,'login.html')
def dooLogin(request):
    if request.method == 'POST':
        user = EmailBackend.authenticate(request,username=request.POST.get('email'),password=request.POST.get('password'))
        if user!=None:
            login(request,user)
            user_type=user.user_type
            if user_type == '1':
                # return HttpResponse('This is HOD pannel')
                return redirect('hodhome') 
            # we got this hodhome from name in path 
            elif user_type == '2':
                return HttpResponse('This is  Staff pannel')
            elif user_type == '3':
                return HttpResponse('This is Student pannel')
            else:
                messages.error(request,'Email and password are invalid')
                return redirect('login')
        else:
            # mess
            messages.error(request,'Email and password are invalid')
            return redirect('login')
def doLogout(request):
    logout(request)

    return redirect('login')