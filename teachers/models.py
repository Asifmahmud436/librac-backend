from django.db import models
from accounts.models import CustomUser
class Teacher(models.Model):
    DESIGNAION_FIELDS =(
        ("Lecturer","Lecturer"),
        ("Assistant Professor","Assistant Professor"),
        ("Resercher Professor","Researcher Professor"),
    )

    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='teacher')
    phone_no = models.IntegerField()
    librac_id = models.IntegerField(unique=True)
    designation = models.CharField(max_length=60,choices=DESIGNAION_FIELDS)
    address = models.TextField()
    image = models.ImageField(upload_to='teachers/images/',blank=True,null=True)

    def __str__(self):
        return self.user.username
