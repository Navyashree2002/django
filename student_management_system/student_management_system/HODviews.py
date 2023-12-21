from email.errors import MessageDefect
from django.shortcuts import redirect,render
# in order to avoid access using link without login
from django.contrib.auth.decorators import login_required

from app.models import Course, CustomUser, Session_Year, Staff, Staff_Notification, Student, Student_Notification, Subject
from django.contrib import messages

# it will redirect to login page itself
@login_required(login_url='/')
def HOME(request):

    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    course_count = Course.objects.all().count()
    subject_count = Subject.objects.all().count()


    student_gender_male = Student.objects.filter(gender='Male').count()
    student_gender_female = Student.objects.filter(gender='Female').count()

    # print(student_gender_male)
    # print(student_gender_female)
    context={
        'student_count':student_count,
        'staff_count':staff_count,
        'course_count':course_count,
        'subject_count':subject_count,
        'student_gender_male':student_gender_male,
        'student_gender_female':student_gender_female,


    }

    return render(request,'HOD/Home.html',context)

@login_required(login_url='/')
def ADD_STUDENT(request):
    course=Course.objects.all()
    session_year=Session_Year.objects.all()
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pict')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        add=request.POST.get('address')
        gender=request.POST.get('gender')
        course_id=request.POST.get('course_id')
        session_year_id=request.POST.get('session_year_id')
    # print(course)
    # print(session_year)
        # print(profile_pic,fname,lname,email,username,password,add,gender,course_id,session_id)
        
        
        # checking email and username
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"email is already taken")
            return redirect('add_student')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,"email is already exists")
            return redirect('add_student')
        else:
            user =CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3,

            )
            user.set_password(password)
            user.save()
            # all the above will be saved in the customuser model

            
            course=Course.objects.get(id = course_id)
            session_year = Session_Year.objects.get(id = session_year_id)


            student = Student(
                admin = user,
                gender = gender,
                address = add,
                session_id = session_year,
                course_id = course,
                
            )
            student.save()

            # messages.success(request,"student record successfully saved")
            messages.success(request,user.first_name + " "  + user.last_name + " successfully added")
            return redirect('add_student')

        
    context={
        'course':course,
        'session_year':session_year,
    }
    return render(request,'HOD/add_student.html/',context)


@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Student.objects.all() # we will get all data from student model
    # print(student)
    context = {
        'student':student
    }
    return render(request,'HOD/view_student.html/',context)

def EDIT_STUDENT(request,id):

    student=Student.objects.filter(id = id)
    course=Course.objects.all()
    session_year=Session_Year.objects.all()

    context={
        'student':student,
        'course':course,
        'session_year':session_year,
    }
    return render(request,'HOD/edit_student.html/',context)

@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == 'POST':
        # profile_pic =request.FILES.get('profile_pict')
        # print(profile_pic)
        student_id= request.POST.get('student_id')
        # print(student_id)

        # user model
        profile_pic = request.FILES.get('profile_pict')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        # student model
        add=request.POST.get('address')
        gender=request.POST.get('gender')
        course_id=request.POST.get('course_id')
        session_year_id=request.POST.get('session_year_id')

        # above thing is to get data 

        # to update user model
        try:
            user=CustomUser.objects.get(id=student_id)
        # user.profile_pic=profile_pic
            user.first_name=first_name
            user.last_name=last_name
            user.email=email
            user.username=username

            # customuser = CustomUser.objects.get(id=request.user.id)

            if password != None and password != "":
                user.set_password(password)

            if profile_pic != None and profile_pic != "":
                user.profile_pic = profile_pic

            user.save()

        # updating student model
            student=Student.objects.get(admin=student_id)
            student.address=add
            student.gender=gender

            course=Course.objects.get(id=course_id)
            student.course_id=course

            session_year=Session_Year.objects.get(id=session_year_id)
            student.session_id=session_year

            student.save()

            messages.success(request,'Successfully Updated' + " " + user.first_name + " " + user.last_name+ " ")
        except:
            messages.error(request,"error while updating")

        #redirect to 
        return redirect('view_student')
    # return render(request,'HOD/edit_student.html')

@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    student=CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request,"successfully deleted" + " "+ student.first_name)
    return redirect('view_student')

    # return render(request,)

@login_required(login_url='/')
def ADD_COURSE(request):
    if request.method == 'POST':
        course_name=request.POST.get('course_name')
        # print(course_name)

        course = Course(
            name =course_name
        )
        course.save()
        messages.success(request,'Courses are successfully created')
        return redirect('add_course')
    return render(request,'HOD/add_course.html')

@login_required(login_url='/')
def VIEW_COURSE(request):
    # to get data
    course=Course.objects.all()
    # print(course)
    context={
        'course':course,
    }
    return render(request,'HOD/view_course.html',context)

@login_required(login_url='/')
def EDIT_COURSE(request,id):
    course=Course.objects.get(id = id)
    context={
        'course':course,
    }
    return render(request,'HOD/edit_course.html',context)

@login_required(login_url='/')
def UPDATE_COURSE(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course_id =request.POST.get('course_id')

        course=Course.objects.get(id = course_id)
        course.name=name
        course.save()
        messages.success(request,'Course are successfully updated')
        return redirect('view_course')



    return render(request,'HOD/edit_course.html')

@login_required(login_url='/')
def DELETE_COURSE(request,id):
    course=Course.objects.get(id=id)
    course.delete()
    messages.success(request,"Courses are successfully deleted")

    return redirect('view_course')

@login_required(login_url='/')
def ADD_STAFF(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pict')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        add=request.POST.get('address')
        gender=request.POST.get('gender')

        # print()

        # now to save in database
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,"email is already taken")
            return redirect('add_staff')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request," This username already exists")
            return redirect('add_staff')
        else:
            user =CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 2,
            )
            user.set_password(password)
            user.save()

            staff = Staff(
                admin = user,
                address = add,
                gender = gender,  
            )
            staff.save()
            messages.success(request,"Successfully added " + " "+ user.first_name)





    return render(request,'HOD/add_staff.html')

@login_required(login_url='/')
def VIEW_STAFF(request):

    staff = Staff.objects.all()

    
    # print(staff)
    context ={
        'staff':staff,
    }
    return render(request,'HOD/view_staff.html',context)


@login_required(login_url='/')
def EDIT_STAFF(request,id):
    staff=Staff.objects.get(id=id)
    context={
        'staff':staff
    }
    return render(request,'HOD/edit_staff.html',context)

@login_required(login_url='/')
def UPDATE_STAFF(request):

    if request.method == 'POST':
        staff_id=request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pict')
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        add=request.POST.get('address')
        gender=request.POST.get('gender')
        
        try:

            user=CustomUser.objects.get(id = staff_id)
            user.first_name=first_name
            user.last_name=last_name
            user.email = email
            user.username=username

        
            if password != None and password != "":
                user.set_password(password)

            if profile_pic != None and profile_pic != "":
                user.profile_pic = profile_pic
            
            if gender == "Select Gender" or gender == "":
                messages.error(request," Please fill gender field of "+ " " + user.first_name+ " to update " )
                return redirect('view_staff')

            else:

                user.save()

                staff =Staff.objects.get(admin = staff_id)
                staff.gender = gender
                staff.address = add

                staff.save()


                messages.success(request,'Successfully updated'+" "+user.first_name + " " + user.last_name)


        except:
            messages.error(request,"error while updating ")

        return redirect('view_staff')

        


    return render(request,'HOD/view_staff.html')

@login_required(login_url='/')
def DELETE_STAFF(request,admin):
    # delete from custom user it will automatically delete from staff 

    staff =CustomUser.objects.get(id = admin)
    staff.delete()
    messages.success(request,"Successfully deleted"+ " " + staff.first_name)
    return redirect('view_staff')


@login_required(login_url='/')
def ADD_SUBJECT(request):

    course = Course.objects.all()
    staff = Staff.objects.all()
    if request.method == 'POST':
        subject_name =request.POST.get('subject_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course=Course.objects.get(id = course_id)
        staff=Staff.objects.get(id = staff_id)

        subject = Subject(
            name = subject_name,
            course = course,
            staff = staff,
        )
        subject.save()
        messages.success(request,'Subject'+ " "+ subject.name+ " "+ " successfully added")
        return redirect('add_subject')

    context = {
        'course':course,
        'staff':staff,
    }
    return render(request,'HOD/add_subject.html',context)


@login_required(login_url='/')
def VIEW_SUBJECT(request):


    subject = Subject.objects.all()

    context = {
        'subject':subject,
    }
    return render(request,'HOD/view_subject.html',context)

@login_required(login_url='/')
def EDIT_SUBJECT(request,id):
    subject = Subject.objects.get(id =id)

    course =Course.objects.all()
    staff =Staff.objects.all()

    context={
        'subject':subject,
        'course':course,
        'staff':staff,
    }

    return render(request,'HOD/edit_subject.html',context)

# @login_required(login_url='/')
def UPDATE_SUBJECT(request):

    if request.method == 'POST':
        subject_id =request.POST.get('subject_id')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')
        subject_name = request.POST.get('subject_name')

        course = Course.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)

        subject = Subject(
            id = subject_id,
            name = subject_name,
            course = course,
            staff =staff,

        )

        # if course == "Select Course" or course == "":
        #         messages.error(request," Please fill Course field of "+ " " + course.name+ " to update " )
        #         return redirect('view_staff')
        subject.save()
        messages.success(request,"Successfully updated "+" "+subject.name+" ")
        return redirect('view_subject')

    return None

def DELETE_SUBJECT(request,id): 
    
    subject =Subject.objects.filter(id=id)
    subject.delete()
    


    messages.success(request,"Subject deleted ")

    return redirect('view_subject')




    return None

def ADD_SESSION(request):

    if request.method == 'POST':
        session_year_start =request.POST.get('session_year_start')
        session_year_end =request.POST.get('session_year_end')

        session = Session_Year(
            session_start = session_year_start,
            session_end = session_year_end,

        )

        session.save()
        messages.success(request,"Successfully created session " )
        return redirect('add_session')

    return render(request,'HOD/add_session.html')


def VIEW_SESSION(request):

    session=Session_Year.objects.all()
    context={
        'session':session,
    }
    return render(request,'HOD/view_session.html',context)

def EDIT_SESSION(request,id):

    session=Session_Year.objects.filter(id=id)

    context={
        'session':session,

    }

    return render(request,'HOD/edit_session.html',context)

def UPDATE_SESSION(request):

    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end= request.POST.get('session_year_end')

        session = Session_Year(
            id = session_id,
            session_start =session_year_start,
            session_end =session_year_end,
        )

        session.save()
        messages.success(request,"Successfully Updated")

        return redirect('view_session')


    return None

def DELETE_SESSION(request,id):

    session =Session_Year.objects.get(id =id)

    session.delete()

    messages.success(request,"successfully deleted")


    return redirect('view_session')

def STAFF_SEND_NOTIFICATION(request):
    staff = Staff.objects.all()
    
    see_notification = Staff_Notification.objects.all().order_by('-id')[0:5]
    s=Staff_Notification.objects.all()

    context={
        'staff':staff,
        'see_notification':see_notification,
        's':s
    }

    return render(request,'HOD/send_staff_noti.html',context)


def STAFF_SAVE_NOTIFICATION(request):
    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')


        staff = Staff.objects.get(admin = staff_id)

        notification = Staff_Notification(

            staff_id = staff,
            message = message
        )
        notification.save()

        messages.success(request," Successfully sent Notification to" + staff.admin.first_name+"" )

        return redirect('staff_send_notification')


    return None

def STUDENT_SEND_NOTIFICATION(request):
    student = Student.objects.all()
    
    see_notification = Student_Notification.objects.all().order_by('-id')[0:5]
    s=Student_Notification.objects.all()

    context={
        'student':student,
        'see_notification':see_notification,
        's':s
    }

    return render(request,'HOD/send_student_noti.html',context)


def STUDENT_SAVE_NOTIFICATION(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        message = request.POST.get('message')


        student = Student.objects.get(admin = student_id)

        notification = Student_Notification(

            student_id = student,
            message = message
        )
        notification.save()

        messages.success(request," Successfully sent Notification to" + student.admin.first_name+"" )

        return redirect('student_send_notification')


    return None














