from app.models import Teams,Sources, Users
from django.db import models


class UserBlocksSources(models.Model):
    source = models.ForeignKey(Sources, default='')
    team = models.ForeignKey(Teams, default='')
    user = models.ForeignKey(Users, default='',related_name="user_blocks")

    class Meta:
        app_label = 'app'
