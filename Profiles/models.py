# -*- coding=utf-8 -*-
import os
from django.db import models
from django.contrib.auth.models import User
import hashlib

class Profile(models.Model):
    """
        Single User Profile
    """
    user = models.ForeignKey(User, related_name="profile_owner")

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
    
    def get_the_avatar_url(self):
        if self.avatar_url:
            return self.avatar_url
        self.avatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(self.email.lower()).hexdigest() + "?s=300"
        return self.avatar_url

    def get_absolute_url(self):
        return "/users/%s/" % self.user.username

    def __str__(self):
        return "%s" % ( self.user.username )
    