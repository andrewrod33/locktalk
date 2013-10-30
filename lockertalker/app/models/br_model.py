from app.models import Teams
from datetime import datetime

from django.db import models

class Br(models.Model):
    date = models.DateTimeField(default=datetime.now())




    class Meta:
        app_label = 'app'

