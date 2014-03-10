#-*- coding: utf-8 -*-
from django.db import models


def handle_file_upload(instance, filename):
    filename = "/users/{0}_{1}".format(int(time()), filename)

class Users(models.Model):
    username = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    email = models.CharField(max_length=255)
    image = models.ImageField(upload_to=handle_file_upload,max_length=255)
    location = models.SlugField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
