from django.contrib import admin
from  .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class Usermodel(UserAdmin):
    list_display = ['username','user_type']
admin.site.register(CustomUser,Usermodel)
admin.site.register(Course)
admin.site.register(Session_Year)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_Notification)
admin.site.register(Student_Notification)
admin.site.register(StudentResult)


