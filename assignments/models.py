from django.db import models
from courses.models import Course

class Assignment(models.Model):
    name = models.CharField(max_length=255)
    marks = models.IntegerField(default=20)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
