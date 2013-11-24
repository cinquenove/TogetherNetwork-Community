# -*- coding=utf-8 -*-
import os
from django.db import models
from django.contrib.auth.models import User

from social_auth.signals import pre_update
from social_auth.backends.facebook import FacebookBackend
from social_auth.backends import google
from social_auth.signals import socialauth_registered
import datetime


class Profile(models.Model):
    """
        Single User Profile
    """
    owner = models.ForeignKey(User, related_name="profile_owner")

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    avatar_url = models.URLField(default="", blank=True)

    #TODO: relation with space by checking other database models ( Bookins, Activities ecc..)
    city = models.CharField(max_length=200, blank=True)
    bio = models.TextField(max_length=500, default="", blank=True)
    skills = models.TextField(max_length=500, default="", blank=True)
    mission = models.CharField(max_length=250, blank=True)
    
    personal_website_url = models.URLField(blank=True)
    twitter_url = models.URLField(default="http://twitter.com/", blank=True)
    facebook_url = models.URLField(default="http://facebook.com/", blank=True)
    
    def get_absolute_url(self):
        return "/users/%s" % self.owner.username

    def __str__(self):
        return "%s" % ( self.owner.username )


def new_users_handler(sender, user, response, details, **kwargs):
    user.is_new = True
    if user.is_new:
        if "id" in response:
            the_avatar_url = None
            if sender == FacebookBackend:
                the_avatar_url = "http://graph.facebook.com/%s/picture?type=large" % response["id"]
            elif sender == google.GoogleOAuth2Backend and "picture" in response:
                the_avatar_url = response["picture"]
            if the_avatar_url:
                the_profile = Profile.objects.get(owner=user)
                if not the_profile:
                    the_profile = Profile()
                    the_profile.owner = user
                the_profile.first_name = user.first_name
                the_profile.last_name = user.last_name
                the_profile.email = user.email
                the_profile.avatar_url = the_avatar_url
                the_profile.save()
    return False

socialauth_registered.connect(new_users_handler, sender=None)