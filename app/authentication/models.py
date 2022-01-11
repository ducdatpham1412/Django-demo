from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_superuser = None
    is_staff = None
    first_name = None
    last_name = None
    groups = None
    user_permissions = None
    email = None
    phone = None

    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=300)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
