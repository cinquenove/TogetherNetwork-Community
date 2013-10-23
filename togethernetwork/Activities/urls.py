# -*- coding=utf-8 -*-

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    #url(r'^', views.search_pillows, name='search_pillows'), #this should be the root
    url(r'^', views.home, name='home'), 

)