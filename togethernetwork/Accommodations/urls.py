# -*- coding=utf-8 -*-

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('', 
    url(r'^(?P<accommodation_pk>\d+)/book$', views.create_new_book_for_accommodation, name='create_new_book_for_accommodation'),
    url(r'^(?P<accommodation_pk>\d+)$', views.single_accommodation_view, name='single_accommodation_view'),

    url(r'^list', views.accommodations_view, name='accommodations_view'), 
    url(r'^$', views.accommodations_view, name='accommodations_view'), 
)




