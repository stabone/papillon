#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# https://docs.djangoproject.com/en/dev/topics/auth/customizing/


def handle_file_upload(instance, filename):
    filename = "/users/{0}_{1}".format(int(time()), filename)

class UsersProfile(models.Model):
    user = models.OneToOneField('auth.User')
    email = models.CharField(max_length=255,unique=True)
    image = models.ImageField(upload_to=handle_file_upload,max_length=255,blank=True,null=True)
    location = models.SlugField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Nepieciešams norādīt epasta adresi')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    user_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    email = models.EmailField(
            verbose_name='Epasts',
            max_length=255,
            unique=True
        )
    image = models.ImageField(
            upload_to=handle_file_upload,
            max_length=255,
            blank=True,
            null=True
        )
    bio = models.TextField()
    is_actice = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'password', 'user_name', 'last_name']

    def get_full_name(self):
        return self.user_name + ' ' + self.last_name

    def get_short_name(self):
        return self.user_name

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
