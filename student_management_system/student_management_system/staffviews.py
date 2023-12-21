from django.shortcuts import redirect, render

from app.models import Course, Session_Year, Staff, Staff_Notification, Student, StudentResult, Subject
from django.contrib import messages

def HOME(request):
    
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()


    student_gender_male = Student.objects.filter(gender = 'Male').count()
    student_gender_female = Student.objects.filter(gender = 'Female').count()
    context={
        'student_count':student_count,
        'staff_count':staff_count,
        'course_count':course_count,
        'subject_count':subject_count,
        'student_gender_male':student_gender_male,
        'student_gender_female':student_gender_female,


    }
    return render(request,'Staff/Home.html',context)

def NOTIFICATIONS(request):
    staff = Staff.objects.filter(admin =  request.user.id)

    for i in staff:
        print(i.id)
        staff_id = i.id

        notifications = Staff_Notification.objects.filter(staff_id = staff_id)

        context={
            'notifications':notifications,
        }



    return render(request,'Staff/notification.html',context)

def STAFF_MARK_AS_DONE(request,status):
    notification = Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()

    return redirect('notifications')

def ADD_RESULT(request):

    staff = Staff.objects.get(admin=request.user.id)
    # print(staff)

    subjects= Subject.objects.filter(staff_id = staff)
    # print(subjects)
    session_year= Session_Year.objects.all()

    action = request.GET.get('action')
    get_subject = None
    get_session = None
    students = None


    if action is not None:
        if request.method == 'POST':
            subject_id=request.POST.get('subject_id')

            session_year_id=request.POST.get('session_year_id')
            # print(subject_id)
            # print(subject_year_id)

            get_subject = Subject.objects.get(id=subject_id)
            get_session = Session_Year.objects.get(id=session_year_id)

            subjects = Subject.objects.filter(id = subject_id)
            # print(subjects)
            for i in subjects:
                student_id = i.course.id
                
                students = Student.objects.filter(course_id = student_id)

    context={
        'subjects':subjects,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session':get_session,
        'students':students,

    }
    return render(request,'Staff/add_result.html',context)


def SAVE_RESULT(request):

    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        mse1 = eval(request.POST.get('mse1'))
        mse2 = eval(request.POST.get('mse2'))
        task = eval(request.POST.get('task'))
        see = eval(request.POST.get('see'))

        cie=mse1+mse2+task
        total = cie + see
        # get_subject = Subject.objects.get(id=subject_id)
        get_session = Session_Year.objects.get(id=session_year_id)

        get_student = Student.objects.get(admin = student_id)
        get_subject = Subject.objects.get(id = subject_id)
        
        subjects = Subject.objects.filter(id = subject_id)
            # print(subjects)
        for i in subjects:
            student_id = i.course.id
                
            students = Student.objects.filter(course_id = student_id)
        
        subjects = Subject.objects.filter(id = subject_id)

        check_exists = StudentResult.objects.filter(subject_id = get_subject,student_id = get_student).exists()
        if(check_exists):
            result = StudentResult.objects.get(subject_id = get_subject,student_id=get_student)
            result.mse1 =mse1
            result.mse2 =mse2
            result.tasks =task
            result.see_marks =see
            

            result.cie = cie

            result.total = total



        



            result.save()
            context={
                'subjects':subjects,
                # 'students':students,
                'get_student':get_student,
                'get_subject':get_subject,
                'get_session':get_session,
                'mse1':mse1,
                'mse2':mse2,
                'task':task,
                'see':see,
                'cie':cie,
                'total':total




            }
            messages.success(request,"successfully updated Results")
            return render(request,'Staff/show_result.html',context)
        else:
            result =StudentResult(
                student_id =get_student,
                subject_id = get_subject,
                mse1 = mse1,
                mse2 = mse2,
                tasks = task,
                cie=cie,
                see_marks= see,
                total = total,

            )
            result.save()


            context={

                'subjects':subjects,
                'students':students,
                'get_subject':get_subject,
                'get_session':get_session,
                'mse1':mse1,
                'mse2':mse2,
                'task':task,
                'see':see,
                'cie':cie,
                'total':total
            }
            messages.success(request,"success")
            return render(request,'Staff/show_result.html',context)

    return None

def SHOW_RESULT(request):

    return render(request,'Staff/show_result.html')