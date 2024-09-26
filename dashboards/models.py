from django.db import models
from students.models import Student
from courses.models import Course

class Dashboard(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,related_name='dashboard')
    drop_course = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.course.name} taken by {self.student.user.username}'
