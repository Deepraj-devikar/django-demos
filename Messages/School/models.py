from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 50)
    password = models.CharField(max_length = 25)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return "(" + str(self.id) + ")" + self.name