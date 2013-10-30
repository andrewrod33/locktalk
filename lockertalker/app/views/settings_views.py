import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from app.models import Teams,Sources,UserBlocksSources
import re



def prefs(request):
    teams = Teams.objects.all().order_by("team_name")
    user = request.session.get('user','NO USER!!!')
    user_teams = user.teams.values_list('id',flat=True)
    print user_teams
    # LOOP THROUGH teams to see if team.team_id matches user_teams, if yes, set something
    data = {
        'teams': teams,
        'user_teams': user_teams
    }
    if request.method == "POST":
        user.teams.clear()
        for key, value in request.POST.iteritems():
            if value is not None:
                print key, value
            t = Teams.objects.get(team_id= value)
            user.teams.add(t)
        return redirect('/settings/sources')


        data['message'] = 'Please Select a Team'

    return render(request, "contact.html", data)

# WHEN THE USER LOGIN, STORE USER, TEAMS and BLOCK SOURCES in SESSION (3 different keys)


def set_sources(request):
    user = request.session.get('user','NO USER!')
    block_sources = request.session.get('block_sources')
    teams = user.teams.all()
    user_blocks = user.user_blocks.values_list('team_id','source_id')
    team_source_blocks = {}
    for team_id,source_id in user_blocks:
        if team_id not in team_source_blocks:
            team_source_blocks[team_id] = []
        team_source_blocks[team_id].append(source_id)
    data = {
            'user':user,
            'team':teams,
            'team_source_blocks': team_source_blocks
    }

    if request.method == "POST":
        UserBlocksSources.objects.all().delete()
        data={'user':user}
        # store users blocks in db
        # when user changes the sources show only those in the db
        # 1. Clear Everything for this user
        # 2. Insert the new set

        for key, value in request.POST.iteritems():
            pattern = re.compile('team_(\d+)_source_(\d+)')
            matches = pattern.match(value)
            team_id = matches.group(1)
            source_id =  matches.group(2)
            data['source_id' ]= source_id
            data['team_id'] = team_id
            UserBlocksSources.objects.get_or_create(**data)
            request.session['block_sources'] = user.user_blocks.all()
        return redirect('/home')
            #print user.user_blocks.values_list('source_id',flat=True)
            #print request.session.get('blocks', 'not block')


    return render(request,'sources.html',data)