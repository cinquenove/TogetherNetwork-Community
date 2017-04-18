# -*- coding=utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^elist$', views.text_email_addresses, name="text_email_addresses"),
    url(r'^edit$', views.edit_profile_view, name='edit_profile_view'),
	url(r'^community', views.community_view, name='community_view'), 
    url(r'^(?P<username>(.*))/$', views.profile_view, name='profile_view'), 
    url(r'^(?P<username>(.*))$', views.profile_view, name='profile_view'), 
]





