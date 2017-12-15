from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'personal/home.html')
    #return HttpResponse('<h1>Emerge the embodiment of Peace and Purity.</h1>')
#return will provide home.html from the template directory.
#Since render will look in template directory
