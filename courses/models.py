from django.db import models
from teachers.models import Teacher



class Course(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=6)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='course')

    def __str__(self):
        return self.name



