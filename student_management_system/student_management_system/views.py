from django.http import HttpResponse
from django.shortcuts import render,redirect

# import EmailBckend.py from app
from app.EmailBackend import EmailBackend
from django.contrib.auth import authenticate,logout,login
#to give error messages
from django.contrib import messages
# in order to avoid access using link without login
from django.contrib.auth.decorators import login_required
# to update profile
from app.models import CustomUser
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
                return redirect('staffhome')
            elif user_type == '3':
                return redirect('studenthome')
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

@login_required(login_url='/')
def Profile(request):
    user=CustomUser.objects.get(id = request.user.id)
    content={
        'user':user
    }
    return render(request,'profile.html',content)
@login_required(login_url='/')
def Profile_Update(request):
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pict')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        # email = request.POST.get('email')
        # username = request.POST.get('username')
        password = request.POST.get('password')
        # print(profile_pic,first_name,last_name,password)
        try:
            customuser = CustomUser.objects.get(id=request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name
            # customuser.profile_pic = profile_pic
            # customuser.profile_pic = profile_pic

            if password != None and password != "":
                customuser.set_password(password)

            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
                
            customuser.save()
            messages.success(request,"Your Profile Updated Successfully !")
            return redirect('profile')
        except:
            messages.error(request,"Failed To Update Your Profile")
        
    return render(request,'profile.html')


