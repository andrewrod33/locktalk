import requests
from django.shortcuts import render
from django.http import HttpResponse
from urlparse import urlparse
from app.models import Teams,Sources
import time

def get_sources(request):
    data = {}
    for a in Teams.objects.all():
        p = requests.get('http://api.espn.com/v1/sports/football/nfl/teams/'+str(a.team_id)+'/news/?apikey=6pz3x9tcb269689jvg23swm8')
        j = p.json()
        i = j["headlines"]
        for k in range(0, len(i)):
            e = i[k]["images"]
            if not e:
                pass
            else:
                time.sleep(0.1)
                source = i[k]["source"]
                print source
                source_model, created = Sources.objects.get_or_create(source_name=source)
                print created
                data ={
                    "team_id": a.team_id,
                    "source_name": source
                }

    for a in Teams.objects.all():
        teams= a.team_name
        b= teams.replace(' ', '-')
        p = requests.get('http://bleacherreport.com/api/front/lead_articles.json?tags='+b+'&devicetype=ipad&appversion=1.4&page=1&perpage=50')
        j = p.json()
        for i in range(0,len(j)):
            time.sleep(.3)
            try:
                e = j[i]['tag']
                url = j[i]['permalink']
                o =urlparse(url, scheme='http',allow_fragments=False )
                pair = o[1]
                if not pair:
                    Sources.objects.get_or_create(source_name= "Bleacher Report")
                else:
                    Sources.objects.get_or_create(source_name=pair)

            except KeyError:
                print "boom"



    return render(request, 'home_og.html', data)
