from django.db import models


class Articles(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255,blank=False)
    description = models.CharField(max_length=255,blank=False)
    article = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
