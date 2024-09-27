from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_ROLES_FIELD = (
        ('Student','Student'),
        ('Teacher','Teacher'),
    )

    user_type = models.CharField(max_length=20,choices=USER_ROLES_FIELD)
