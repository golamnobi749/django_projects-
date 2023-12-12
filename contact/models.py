from django.db import models

# Create your models here.
class Result(models.Model):
    student_id = models.CharField(max_length=30)
    student_name = models.CharField(max_length=50)
    students_father_name = models.CharField(max_length=100)
    
    students_mother_name = models.CharField(max_length=50)
    bangla = models.CharField(max_length=30)
    math = models.CharField(max_length=30)
    english = models.CharField(max_length=30)
    science = models.CharField(max_length=30)
    social = models.CharField(max_length=30)
    religuion = models.CharField(max_length=30)


