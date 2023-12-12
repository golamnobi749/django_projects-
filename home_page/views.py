from django.shortcuts import render
from . models import Student


# Create your views here.
def home(request):
    return render(request,'home_page/main.html')

def student(request):
    student_info = Student.objects.all()
    return render(request,'home_page/student.html', {'students':student_info})