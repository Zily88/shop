from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class ShopUser(AbstractUser):
    phone_number = models.CharField(max_length=10, verbose_name='mobile number')