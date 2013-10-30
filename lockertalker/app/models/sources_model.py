from django.db import models


class Sources(models.Model):
    source_name = models.CharField(max_length=255, unique=True)

    class Meta:
        app_label = 'app'

    def __unicode__(self):
        return self.source_name

