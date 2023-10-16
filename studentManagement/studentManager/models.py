from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name   

class Grade(models.Model):
    name = models.CharField(max_length=10, unique=True)
    subjects = models.ManyToManyField(Subject)
    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=50)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    year = models.CharField(max_length=10, choices=[('I', '1'), ('II', '2')], default='I')
    def __str__(self):
        return self.name

class Student(models.Model):
    
    student_name = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=50)
    student_phone = models.CharField(max_length=11)
    parent_phone = models.CharField(max_length=11)
    enrolled_class = models.ForeignKey(Class, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.student_name
