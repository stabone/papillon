from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.question

class Choise(models.Model):
    poll_id = models.ForeignKey(Poll)
    option  = models.CharField(max_length=255)
    choise_type = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.option

