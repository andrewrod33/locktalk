from django.db import models
from app.models import Teams, Sources
from datetime import datetime


class News(models.Model):
    headline = models.CharField(max_length=255,default='')
    link = models.URLField(max_length=300)
    description = models.CharField(max_length=255,default='')
    images = models.CharField(max_length=255, default='', null=True)
    team = models.ForeignKey(Teams, null=True, to_field="team_id")
    date = models.DateTimeField(default=datetime.now())
    source = models.ForeignKey(Sources, null=True, to_field="id")
    source_name = models.CharField(max_length=255, default='')

    class Meta:
        app_label = 'app'
