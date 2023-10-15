from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

class Student(models.Model):
    student_name = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=50)

    student_phone = models.CharField(max_length=11)
    parent_phone = models.CharField(max_length=11)
    grades = [('pre_eng','pre_eng'),('ics_stat','ics_stat'),('ics_cs','ics_cs'),('pre_med','pre_med')]
    grade = models.CharField(max_length=10,choices=grades)
    years =[('I','1'),('II','2')]
    year = models.CharField(max_length = 10, choices=years, default='I')
   

    
    def __str__(self):
        return self.student_name
