# -*- coding=utf-8 -*-

from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    # Single Activity 
    url(r'^(?P<activity_pk>\d+)/delete$', views.delete_activity, name='delete_activity'),
    url(r'^(?P<activity_pk>\d+)/leave$', views.leave_activity, name='leave_activity'),
    url(r'^(?P<activity_pk>\d+)/join$', views.join_activity, name='join_activity'),
    url(r'^(?P<activity_pk>\d+)/edit$', views.edit_activity_view, name='edit_activity_view'),
    url(r'^(?P<activity_pk>\d+)/comment$', views.new_activity_comment, name='new_activity_comment'),
    url(r'^(?P<activity_pk>\d+)/(?P<slug>[-\w]+)/$', views.single_activity_view, name='single_activity_view'),
    url(r'^(?P<activity_pk>\d+)/(?P<slug>[-\w]+)$', views.single_activity_view, name='single_activity_view'),
    url(r'^(?P<activity_pk>\d+)/(?P<slug>[-\w]+)/delete$', views.delete_activity, name='delete_activity'),
    url(r'^(?P<activity_pk>\d+)/(?P<slug>[-\w]+)/leave$', views.leave_activity, name='leave_activity'),
    url(r'^(?P<activity_pk>\d+)/(?P<slug>[-\w]+)/join$', views.join_activity, name='join_activity'),
    url(r'^(?P<activity_pk>\d+)/(?P<slug>[-\w]+)/edit$', views.edit_activity_view, name='edit_activity_view'),
    url(r'^(?P<activity_pk>\d+)/(?P<slug>[-\w]+)/comment$', views.new_activity_comment, name='new_activity_comment'),
    url(r'^(?P<activity_pk>\d+)/$', views.single_activity_view, name='single_activity_view'),
    url(r'^(?P<activity_pk>\d+)$', views.single_activity_view, name='single_activity_view'),
    # Multiple Activities
    url(r'^new', views.edit_activity_view, name='edit_activity_view'),
    url(r'^list', views.activities_view, name='activities_view'),
    url(r'^$', views.activities_view, name='activities_view'),
)




