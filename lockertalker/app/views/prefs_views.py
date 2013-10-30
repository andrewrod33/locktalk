import requests
from django.shortcuts import render
from django.http import HttpResponse
from app.models import Teams,News,Sources,PersonalizedSource
import requests


def get_prefs(request):
    user = request.session.get('user','NO USER!!!')
    #user2 = user.id
    #sources = PersonalizedSource.objects.get_pref(user2)
    #block = Block.objects.all()
    #print block
    if request.method == "POST":
            #user.teams.clear()
            for key, value in request.POST.iteritems():
                print key, value
                t = Sources.objects.get(id= value)
                print t.id
            #    # source = EspnSources.objects.get(source_name=value)
            #    # u = Users.objects.get(facebook_uid=100006525518315)

                y = user.teams.add()
                print y
                # user.teams.add(source)

    #data = {'sources':sources}
    return render(request, "sources.html", data)

    #data = {
    #    'teams': Teams.objects.all(),
    #    'sources': Sources.objects.all()
    ##}
    #teams = Teams.objects.filter()
    #sources = Sources.objects.filter()
    #for each in user.teams.all():
    #    print each.team_id

        #for each in teams.sources


    #for i in range(0,len(sources)):
    #    source_name= sources[i].source_name
    #    source_id =sources[i].p_id
    #    print source_id
    #    print source_name
        #data.append(source_id)
    #    stuff={'source_id':source_name}

