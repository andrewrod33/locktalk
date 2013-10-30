from django.db import models
from app.models import Sources


class Teams(models.Model):
    team_name = models.CharField(max_length=255)
    team_id = models.IntegerField(unique=True)
    sources = models.ManyToManyField(Sources)


    class Meta:
        app_label = 'app'

    def __unicode__(self):
        return '%s (%s)' % (self.team_name, self.id)
