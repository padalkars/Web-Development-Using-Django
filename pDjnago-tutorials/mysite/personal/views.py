from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<title>Shrikrishna</title><H1>I am a powerful soul.</H1>')
