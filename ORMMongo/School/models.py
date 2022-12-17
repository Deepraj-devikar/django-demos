from django.db import models

class Student(models.Model):
    studentName = models.CharField(max_length = 150)
    studentEmail = models.EmailField(max_length=254)
    rollNumber = models.IntegerField()
    
    def __str__(self):
        return "("+self.rollNumber+") "+self.studentName

class Teacher(models.Model):
    teacher_name = models.CharField(max_length = 150)
    teacher_email = models.EmailField(max_length=254)
    roll_number = models.IntegerField()

    def __str__(self):
        return "("+self.roll_number+") "+self.teacher_name