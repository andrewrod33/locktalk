import requests
from django.shortcuts import render
from django.http import HttpResponse
from app.models import Teams,Sources, News



def user(request):
    request.session["user_id"]= "1"
    return HttpResponse("yo")