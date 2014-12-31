from django.db import models
from django.conf import settings

from helper.utils import random_string


def handle_file_upload(instance, filename):
    filename = "/badges/{1}-{2}".format(
                            random_string(max=10), filename)

    return filename


class Badges(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-title']


class BadgeUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    badge = models.ForeignKey(Badges)
    created_at = models.DateTimeField(auto_now_add=True)


