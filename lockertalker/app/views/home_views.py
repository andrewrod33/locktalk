from app.models import News,UserBlocksSources, Sources
from django.shortcuts import redirect
from django.shortcuts import render
import re

def home(request):
    data = []
    user = request.session.get('user','NO USER!!!')
    teams = user.teams.all()
    user_blocks = user.user_blocks.values_list('team_id','source_id')
    print 'User blocking: %s' % user_blocks
    team_source_blocks ={}
    sources = Sources.objects.all()

    for team_id,source_id in user_blocks:
        if team_id not in team_source_blocks:
            team_source_blocks[team_id] = []
        team_source_blocks[team_id].append(source_id)

    for team in teams:
        news = News.objects.filter(team_id=team.team_id).order_by('date').reverse()
        print 'Team %s has %s news' % (team.team_name,len(news))

        if team.team_id in team_source_blocks:
            filter_news = news.exclude(source_id__in=team_source_blocks[team.id])
            data.append(filter_news)
        else:
            data.append(news)


    if request.method == "POST":
        blocks={'user':user}
        for key, value in request.POST.iteritems():
            pattern = re.compile('team_(\d+)_source_(\d+)')
            matches = pattern.match(value)
            team_id = matches.group(1)
            source_id =  matches.group(2)
            blocks['source_id' ]= source_id
            blocks['team_id'] = team_id
            UserBlocksSources.objects.get_or_create(**blocks)
            request.session['block_sources'] = user.user_blocks.all()
        return redirect('/home')

    stuff= {'news':data, 'sources':sources, 'teams':user.teams.all()}


    return render(request, 'news.html', stuff)
