from django.shortcuts import redirect,render

def HOME(request):
    return render(request,'HOD/Home.html')