
# Create your views here.

from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index')
]

