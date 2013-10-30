from django.http import HttpResponse
from app.models import Teams,Sources,News
import requests
import time


def teams_sources(request):
    data = {
        'teams': Teams.objects.all(),
        'sources': Sources.objects.all()
    }

    for i in News.objects.all():
        team = i.team_id
        source = i.source_id

        teams.sources.add()



    return HttpResponse('yo')
