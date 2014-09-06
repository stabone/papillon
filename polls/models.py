#-*- coding: utf-8 -*-
from django.db import models
from django.conf import settings


# Create your models here.
class Polls(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    public = models.BooleanField(default=True)
    poll = models.CharField(max_length=255, db_index=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        permissions = (
            ('add_poll', 'Pievienot aptauju'),
            ('edit_poll', 'Labot aptauju'),
            ('edit_poll_content', 'Labot aptauju saturu'),
            ('delete_poll', 'Dzēst aptauju'),
            ('save_poll_results', 'Saglabāt aptaujas rezultātus'),
            ('take_poll', 'Aptauja'),
        )

    def __unicode__(self):
        return self.poll


class Questions(models.Model):
    poll = models.ForeignKey(Polls, db_index=True)
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ('add_question', 'Pievienot jautājumu'),
            ('edit_question', 'Labot jautājumu'),
            ('delete_question', 'Dzēst jautājumu'),
        )

    def __unicode__(self):
        return self.question


class Choises(models.Model):
    question = models.ForeignKey(Questions, db_index=True)
    option = models.CharField(max_length=255)
    choise_type = models.IntegerField(default=0)
    correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ('add_choise', 'Pievienot izvēli'),
            ('edit_choise', 'Labot izvēli'),
            ('delete_choise', 'Dzēst izvēli'),
        )

    def __unicode__(self):
        return self.option


"""
for now these fields will be integers
"""
class Results(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    #poll = models.ForeignKey(Polls)
    poll = models.PositiveIntegerField()
    #question = models.ForeignKey(Questions)
    question = models.PositiveIntegerField()
    #answer = models.ForeignKey(Choises)
    answer = models.PositiveIntegerField()
    correct = models.BooleanField(default=False)

