from django.db import models
from app.models import Teams


class Users(models.Model):
    facebook_uid = models.CharField(max_length=255, default='')
    user = models.CharField(max_length=255, default='')
    facebook_access_token = models.CharField(max_length=255, default='')
    facebook_access_token_expires = models.CharField(max_length=255, default='')
    teams= models.ManyToManyField(Teams)

    def __unicode__(self):
        return self.user

    class Meta:
        app_label = 'app'

