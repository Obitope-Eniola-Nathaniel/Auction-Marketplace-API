from django.contrib.auth.models import AbstractUser
from django.db import models

from .choices import UserRole


class User(AbstractUser):

    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.USER, )

    def __str__(self):
        return self.username