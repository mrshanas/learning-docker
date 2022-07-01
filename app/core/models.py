from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)

class UserManager(BaseUserManager):
    """Manager for users"""

    def create_user(self,email,password=None,**extra_fields):
        """Create, save and return a new user"""
        if not email:
            raise ValueError('Please provide an email address')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self,email,password=None,**extra_fields):
        """Create, save and return a new superuser"""
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_staff',True)
        superuser = self.create_user(email,password,**extra_fields)

        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
