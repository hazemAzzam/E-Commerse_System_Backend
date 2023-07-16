from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import MemberManager

# Create your models here.
class Member(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True)
    fname = models.CharField(max_length=50)
    minit = models.CharField(max_length=50, null=True, blank=True)
    lname = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname']

    objects = MemberManager()

    def __str__(self):
        return self.email