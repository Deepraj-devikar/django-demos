from django.db import models

class Student(models.Model):
    student_name = models.CharField(max_length = 150)
    student_email = models.EmailField(max_length=254)
    roll_number = models.IntegerField()
    
    def __str__(self):
        return "("+str(self.roll_number)+") "+self.student_name

class Teacher(models.Model):
    teacher_name = models.CharField(max_length = 150)
    teacher_email = models.EmailField(max_length=254)
    roll_number = models.IntegerField()

    def __str__(self):
        return "("+str(self.roll_number)+") "+self.teacher_name