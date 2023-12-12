from django.contrib import admin
from . models import Student
# Register your models here.
class studentAdmin(admin.ModelAdmin):
    list_display = ('id','student_id','student_name','student_gmail','student_class','course','batch')
admin.site.register(Student,studentAdmin)