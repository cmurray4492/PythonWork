from django.db import models
from . managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class CustomUser(AbstractBaseUser, PermissionsMixin):

    username = None
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=80, blank=True)
    last_name = models.CharField(max_length=135, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    is_writer = models.BooleanField(default=False, verbose_name="Are you a writer?")

    USERNAME_FIELD = 'email'
    RQEQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
