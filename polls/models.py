#-*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Polls(models.Model):
    user = models.OneToOneField('auth.User')
    poll = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.poll


class Questions(models.Model):
    poll = models.ForeignKey(Polls, db_index=True)
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.question


class Choises(models.Model):
    question = models.ForeignKey(Questions, db_index=True)
    option = models.CharField(max_length=255)
    choise_type = models.IntegerField(default=0)
    correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.option


"""
for now these fields will be integers
"""
class Results(models.Model):
    user_id = models.ForeignKey('auth.User')
    #poll_id = models.ForeignKey(Polls)
    poll_id = models.PositiveIntegerField()
    #question_id = models.ForeignKey(Questions)
    question_id = models.PositiveIntegerField()
    #answer_id = models.ForeignKey(Choises)
    answer_id = models.PositiveIntegerField()

