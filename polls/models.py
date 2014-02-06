from django.db import models


# Create your models here.
class Polls(models.Model):
    poll = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.poll


class Questions(models.Model):
    poll_id = models.ForeignKey(Polls, db_index=True)
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.question


class Choises(models.Model):
    poll_id = models.ForeignKey(Questions, db_index=True)
    option  = models.CharField(max_length=255)
    choise_type = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.option

