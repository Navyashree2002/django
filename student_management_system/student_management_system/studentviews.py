

from django.shortcuts import redirect, render

from app.models import Student, Student_Notification, StudentResult


def HOME(request):
    return render(request,'Student/Home.html')

def NOTIFICATIONS(request):
    student = Student.objects.filter(admin =  request.user.id)

    for i in student:
        # print(i.id)
        student_id = i.id

        notifications = Student_Notification.objects.filter(student_id = student_id)

        context={
            'notifications':notifications,
        }



    return render(request,'Student/notification.html',context)

def STUDENT_MARK_AS_DONE(request,status):
    notification = Student_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()

    return redirect('notifications')


def VIEW_RESULT(request):

    student =Student.objects.get(admin = request.user.id)

    result = StudentResult.objects.filter(student_id=student)
    for i in result:
        total = i.total
    context= {
        'result':result,
        'total':total,
    }
    return render(request,'Student/view_result.html',context)