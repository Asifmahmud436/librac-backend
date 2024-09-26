from django.db import models
from accounts.models import CustomUser
class Student(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='student')
    phone_no = models.IntegerField()
    librac_id = models.IntegerField(unique=True)
    address = models.TextField()
    image = models.ImageField(upload_to='students/images/',blank=True,null=True)

    def __str__(self):
        return self.user.username
