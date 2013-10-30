from django.http import HttpResponse

import requests

from app.models import Teams

from django.shortcuts import render

def get_espn(request):
    data = {}
    p = requests.get('http://api.espn.com/v1/sports/football/nfl/teams?apikey=6pz3x9tcb269689jvg23swm8')
    r = p.json()
    f = r["sports"][0]["leagues"][0]["teams"]
    print f
    for i in range(0, len(f)):
        name = f[i]["location"] +' ' + f[i]["name"]
        id = f[i]["id"]

        # data={ name : id }
        # print data
        Teams.objects.get_or_create(team_name=name, team_id=id)
        # url = "http://api.espn.com/v1/sports/football/nfl/teams/13/news/?apikey=6pz3x9tcb269689jvg23swm8"

        # request = requests.get('http://api.espn.com/v1/sports/football/nfl/teams/13/news/?apikey=6pz3x9tcb269689jvg23swm8')
        # alot = request.json()
        # print alot[0]

    # return t_name
    # return t_id
    #trying to get team ids and team name from the api
    # return HttpResponse()
    return render(request, "home_og.html", data)



# http://api.espn.com/v1/sports/football/nfl/teams?apikey=6pz3x9tcb269689jvg23swm8