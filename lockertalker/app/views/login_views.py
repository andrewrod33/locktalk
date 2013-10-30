from django.http import HttpResponse
from app.models import News
import requests

from django.shortcuts import render

def login(request):
    news = News.objects.all().order_by('date').reverse()
    host = request.get_host()
    #print host
    facebook_auth_dialog = 'https://www.facebook.com/dialog/oauth?client_id=708478032501977&redirect_uri='
    facebook_auth_dialog += 'http://'+host+'/facebook'
    #print facebook_auth_dialog
    data= {
        'facebook_auth_dialog': facebook_auth_dialog,
        'news':news
    }
    return render(request, "index.html", data)