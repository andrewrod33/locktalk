import httplib2
import urllib
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils import simplejson as json
from django.shortcuts import render
from app.models import Users
import requests

def facebook(request):
    host = request.get_host()
    """

    :param request:
    :return:
    """
    params = {
        'client_id': settings.FACEBOOK_APP_ID,
        'redirect_uri': 'http://'+host+'/facebook',
        'client_secret': settings.FACEBOOK_SECRET_KEY,
        'code': request.GET['code']
    }

    http = httplib2.Http(timeout=15)
    response, content = http.request('https://graph.facebook.com/oauth/access_token?%s' % urllib.urlencode(params))
    print response
    print content
    # Find access token and expire (this is really gross)
    params = content.split('&')
    ACCESS_TOKEN = params[0].split('=')[1]
    EXPIRE = params[1].split('=')[1]

    # Get basic information about the person
    response, content = http.request('https://graph.facebook.com/me?access_token=%s' % ACCESS_TOKEN)
    data = json.loads(content)
    # Try to find existing profile, create a new user if one doesn't exist
    try:
        user = Users.objects.get(facebook_uid=data['id'])
        #request.session['data']=data
        # print request.session.get('data','not working')
    except Users.DoesNotExist:
        user = Users()
        user.facebook_uid = data['id']
        user.user = data['name']
        user.facebook_access_token = ACCESS_TOKEN
        user.facebook_access_token_expires = EXPIRE
        user.save()

        #login(request, user)

    request.session['user'] = user
    request.session['block_sources'] = "initial"
    print request.session.get('user', 'Not working')

    # # Authenticate and log user in
    #     user = authenticate(username=profile.user.username, password=profile.facebook_uid)

    return HttpResponseRedirect('/home')
    # return render(request, "settings.html", data)