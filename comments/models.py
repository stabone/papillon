#-*- coding: utf-8 -*-
from django.db import models

from courses.models import Materials
from polls.models import Polls


""" this stuff cound couse cyclic import """
class MaterialComments(models.Model):
    material = models.ForeignKey(Materials)
    # user = this should come from session
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PollComments(models.Model):
    poll = models.ForeignKey(Polls)
    # user = user identifier
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


