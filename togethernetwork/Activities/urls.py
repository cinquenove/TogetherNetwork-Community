# -*- coding=utf-8 -*-

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    # Single Activity
    url(r'^(?P<activity_pk>\d+)/edit$', views.edit_activity_view, name='edit_activity_view'),
    url(r'^(?P<activity_pk>\d+)/$', views.single_activity_view, name='single_activity_view'),
    url(r'^(?P<activity_pk>\d+)$', views.single_activity_view, name='single_activity_view'),
    # Multiple Activities
    url(r'^new', views.edit_activity_view, name='edit_activity_view'),
    url(r'^list', views.activities_view, name='activities_view'),
)




