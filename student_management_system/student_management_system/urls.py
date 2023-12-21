"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views,HODviews,staffviews,studentviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),
    # login path
    path('',views.LOGIN,name='login'),
    path('dologin',views.dooLogin,name="doLogin"),
    path('dologout',views.doLogout,name="logout"),
    #profile update
    path('/profile/',views.Profile,name="profile"),
    path('/profile/update/',views.Profile_Update,name="profile_update"),

    #hod pannel

    # for student
    path('HOD/Home',HODviews.HOME,name='hodhome'),
    path('HOD/Student/Add',HODviews.ADD_STUDENT,name='add_student'),
    path('HOD/Student/View',HODviews.VIEW_STUDENT,name='view_student'),
    path('HOD/Student/Edit/<str:id>',HODviews.EDIT_STUDENT,name='edit_student'),
    path('HOD/Student/Update',HODviews.UPDATE_STUDENT,name='update_student'),
    path('HOD/Student/Delete/<str:admin>',HODviews.DELETE_STUDENT,name='delete_student'),

    # for staff
    path('HOD/Staff/Add',HODviews.ADD_STAFF,name="add_staff"),
    path('HOD/Staff/View',HODviews.VIEW_STAFF,name="view_staff"),
    path('HOD/Staff/Edit<str:id>',HODviews.EDIT_STAFF,name="edit_staff"),
    path('HOD/Staff/Update',HODviews.UPDATE_STAFF,name="update_staff"),
    path('HOD/Staff/Delete<str:admin>',HODviews.DELETE_STAFF,name="delete_staff"),

#course
    path('HOD/Course/Add',HODviews.ADD_COURSE,name='add_course'),
    path('HOD/Course/View',HODviews.VIEW_COURSE,name='view_course'),
    path('HOD/Course/Edit<str:id>',HODviews.EDIT_COURSE,name='edit_course'),
    path('HOD/Course/Update',HODviews.UPDATE_COURSE,name='update_course'),
    path('HOD/Course/Delete/<str:id>',HODviews.DELETE_COURSE,name='delete_course'),



    path('HOD/Subject/Add',HODviews.ADD_SUBJECT,name='add_subject'),
    path('HOD/Subject/View',HODviews.VIEW_SUBJECT,name='view_subject'),
    path('HOD/Subject/Edit<str:id>',HODviews.EDIT_SUBJECT,name='edit_subject'),
    path('HOD/Subject/Update',HODviews.UPDATE_SUBJECT,name='update_subject'),
    path('HOD/Subject/Delete<str:id>',HODviews.DELETE_SUBJECT,name='delete_subject'),




    path('HOD/Session/Add',HODviews.ADD_SESSION,name='add_session'),
    path('HOD/Session/View',HODviews.VIEW_SESSION,name='view_session'),
    path('HOD/Session/Edit<str:id>',HODviews.EDIT_SESSION,name='edit_session'),
    path('HOD/Session/Update',HODviews.UPDATE_SESSION,name='update_session'),
    path('HOD/Session/Delete<str:id>',HODviews.DELETE_SESSION,name='delete_session'),


    path('HOD/Staff/Send_Notification',HODviews.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
    path('HOD/Student/Send_Notification',HODviews.STUDENT_SEND_NOTIFICATION,name='student_send_notification'),
    path('HOD/Staff/Save_Notification',HODviews.STAFF_SAVE_NOTIFICATION,name='staff_save_notification'),
    path('HOD/Student/Save_Notification',HODviews.STUDENT_SAVE_NOTIFICATION,name='student_save_notification'),


    # staff pannel
        path('Staff/Home',staffviews.HOME,name='staffhome'),
        path('Staff/Notifications',staffviews.NOTIFICATIONS,name='notifications'),
        path('Staff/mark_as _done<str:status>',staffviews.STAFF_MARK_AS_DONE,name='staff_mark_as_done'),
        path('Staff/Add_Result',staffviews.ADD_RESULT,name='add_result'),
        path('Staff/Save_Result',staffviews.SAVE_RESULT,name='save_result'),
        path('Staff/Show_Result',staffviews.SHOW_RESULT,name='show_result'),

        
        
        
        
        
        path('Student/Home',studentviews.HOME,name='studenthome'),
        path('Student/Notifications',studentviews.NOTIFICATIONS,name='notifications'),
        path('Student/mark_as _done<str:status>',studentviews.STUDENT_MARK_AS_DONE,name='student_mark_as_done'),
        path('Student/View_Result',studentviews.VIEW_RESULT,name='view_result'),
        











] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

