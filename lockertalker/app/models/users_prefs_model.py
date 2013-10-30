import requests
from django.shortcuts import render
from django.http import HttpResponse
from app.models import Teams,News,Sources
import requests

from django.db import models


class SourceManager(models.Manager):
    def get_pref(self,id):

        # return HttpResponse('yo')
        from django.db import connection
        cursor = connection.cursor()
        cursor.execute("""
            select s.id, s.source_name
            from app_teams_sources ts
            left join app_sources s on s.id = ts.sources_id
            where ts.teams_id in (select teams_id from app_users_teams where users_id = %s)
        """ %(id))

        result_list = []
        print 'printing everything'
        for row in cursor.fetchall():
            #print row

            p = self.model(p_id=row[0],source_name=row[1])
            #print p
            result_list.append(p)

        return result_list

class PersonalizedSource(models.Model):
    p_id = models.IntegerField(default='')
    source_name = models.CharField(max_length=255, default='')
    objects = SourceManager()
    class Meta:
        app_label = 'app'
        #def __unicode__(self):
        #     return self.source_name

# select s.id, s.source_name
# from app_teams_sources ts
# left join app_sources s on s.id = ts.sources_id
# where ts.teams_id in (select teams_id from app_users_teams where users_id = 1);