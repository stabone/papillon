#-*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser

# https://docs.djangoproject.com/en/dev/topics/auth/customizing/


def handle_file_upload(instance, filename):
    filename = "/users/{1}".format(filename)


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

    def create_superuser(self, email, password, user_name, last_name):
        user = self.create_user(
            email,
            password=password
        )
        user.user_name=user_name
        user.last_name=last_name
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    user_name = models.CharField(verbose_name='Vārds', max_length=128)
    last_name = models.CharField(verbose_name='Uzvārds', max_length=128)

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
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    # 1 => basic user, 2 => author, 3 => adminstrator
    user_type = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'last_name']

    def get_avatar(self):
        return self.image if self.image else '/media/users/default.svg'

    def get_full_name(self):
        full_name = "%s %s" % (self.user_name, self.last_name)

        return full_name.strip()

    def get_short_name(self):
        return self.user_name

    def get_email(self):
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

