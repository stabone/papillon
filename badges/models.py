from django.db import models
from django.conf import settings

from helper.utils import random_string


def handle_file_upload(instance, filename):
    filename = "/badges/{1}.{2}".format(
                            random_string(max=10), file_format)

    return filename


class BadgeTypes(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


class Badges(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    badge = models.ForeignKey(BadgeTypes)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # unique = user_id and badge
    class Meta:
        ordering = ['-created_at']

