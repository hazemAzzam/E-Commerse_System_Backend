from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import MemberManager
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Member(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=50)
    
    picture = models.ImageField(upload_to='images/', null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = MemberManager()

    def __str__(self):
        return self.email
    
class Recover_Code(models.Model):
    code = models.CharField(max_length=50)