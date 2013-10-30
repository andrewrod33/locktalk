import requests
from django.shortcuts import render
from django.http import HttpResponse
from app.models import Teams,News,Sources
import time


def get_news(request):
    for a in Teams.objects.all():
        time.sleep(.3)
        f = a.team_id
        p = requests.get('http://api.espn.com/v1/sports/football/nfl/teams/'+str(a.team_id)+'/news/?apikey=6pz3x9tcb269689jvg23swm8')
        j = p.json()
        # i = j["headlines"]
        for h in j['headlines']:
            data = {
                'team_id': a.team_id,
                'link': h["links"]["web"]["href"],
                'headline': h["linkText"],
                'date': h["published"],
                'description': h.get('description',''),
                'source_name':h.get('source', '')
            }

            print h.get('images')

            # images
            if h.get('images') is not None and len(h.get('images')) != 0:
                data['images'] = h.get('images')[0]['url']

            # source
            # Figure out what's the current source
            source = h.get('source')
            source_item, created = Sources.objects.get_or_create(source_name=source)
            print source_item
            print created

            data['source_id'] = source_item.id
            #print data
            # save to DB
            news_item, created = News.objects.get_or_create(**data)

            print news_item
            print created

    return HttpResponse("yo")
