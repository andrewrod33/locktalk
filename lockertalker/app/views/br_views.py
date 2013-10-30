import requests
from django.shortcuts import render
from django.http import HttpResponse
from app.models import Teams,Br, News,Sources
from urlparse import urlparse
import time

def get_br1(request):
    for a in Teams.objects.all():
        teams= a.team_name
        b= teams.replace(' ', '-')
        p = requests.get('http://bleacherreport.com/api/front/lead_articles.json?tags='+b+'&devicetype=ipad&appversion=1.4&page=1&perpage=50')
        j = p.json()
        for i in range(0,len(j)):
            time.sleep(.3)
            try:
                e = j[i]['tag']
                data= {
                    'team_id': a.team_id,
                    'headline': j[i]['title'],
                    'images' : j[i]['primary_image_650x440']
                }
                url = j[i]['permalink']
                o =urlparse(url, scheme='http',allow_fragments=False )
                pair = o[1]
                if not pair:
                    source ="Bleacher Report"
                    source_item, created = Sources.objects.get_or_create(source_name=source)
                    # print created
                    add = "http://bleacherreport.com/articles/"+url
                    data['link'] = add
                    data['source_id'] = source_item.id
                    data['source_name'] = source
                    a.sources.add(source_item.id)
                else:
                    data['link']= url
                    source = pair
                    source_item, created = Sources.objects.get_or_create(source_name = pair)
                    data['source_id']= source_item.id
                    data['source_name']= pair
                    a.sources.add(source_item.id)
                news_item, created = News.objects.get_or_create(**data)
            except KeyError:
                pass
    return HttpResponse('yo')
