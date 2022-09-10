from django.contrib.auth import AbstractBaseUser, BaseManager
from django.db import models


class CustomUser(AbstractBaseUser):
     email = models.EmailField(unique=True, max_length=100)
