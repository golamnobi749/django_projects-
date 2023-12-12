from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=30)
    student_gmail = models.CharField(max_length=50)
    student_class = models.CharField(max_length=50)
    course = models.IntegerField()
    batch = models.IntegerField()




