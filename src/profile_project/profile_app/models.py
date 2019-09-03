# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.conf import settings


# Create your models here.
class UserProfileManager(BaseUserManager):
    """Helps Django works with our own custom user model"""

    def create_user(self,email,name,password=None):

        if not email:
            raise ValueError("User must have an email address.")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """ Create and saves a new super user with given details."""

        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user




class UserProfile(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=220,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
