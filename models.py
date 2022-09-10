from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
     def create_user(self, email, password=None, first_name=None, last_name=None, department=None):
          if not email:
               raise ValueError("Users must have an email")
          if not password:
               raise ValueError("Users must have a password")
          if password1 != password2:
               raise ValueError("password1 and password 2 not the same")
           
          user = self.model(email = self.normalize_email(email)
                            department = department
                            first_name = first_name
                            last_name = last_name
                            )
          user.set_password(password)
          user.save(using=self._db)
          return user
     
     def create_superuser(self):
          pass
     # continue from here next time also don't forget to add forms and email confirmation logic
          
                            



class CustomUser(AbstractBaseUser):
     email = models.EmailField(unique=True, max_length=100)
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     department = models.CharField(max_length=50)
     _admin = models.BooleanField(default=False, verbose_name="admin")
     _staff = models.BooleanField(default=False, verbose_name="staff")
     _active = models.BooleanField(default=False, verbose_name="active")
     date_joined = models.DateField(auto_now_add=True)
     
     USERNAME_FIELD = "email"
     REQUIRED_FIELDS = []
     
     objects = CustomUserManager()
     
     def has_perm(self):
          return self._admin
     
     def has_module_perm(self):
          return True
     
     @property
     def is_admin(self):
          return self._admin
     
     @is_admin.setter
     def is_admin(self, bool):
          self._admin = bool
     
     @property
     def is_active(self):
          return self._active
     
     @is_active.setter
     def is_active(self, bool):
          self._active = bool
     
     @property
     def is_staff(self):
          return self._staff
     
     @is_staff.setter
     def is_staff(self, bool):
          self._staff = bool
     
     
