# -*- coding=utf-8 -*-
import os
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
        Single User Profile
    """
    owner = models.ForeignKey(User, related_name="profile_owner")

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)

    #TODO: relation with space by checking other database models ( Bookins, Activities ecc..)
    city = models.CharField(max_length=200)
    bio = models.TextField(max_length=500, default="")
    skills = models.TextField(max_length=500, default="")
    mission = models.CharField(max_length=250)
    
    personal_website_url = models.URLField(blank=True)
    twitter_url = models.URLField(default="http://twitter.com/", blank=True)
    facebook_url = models.URLField(default="http://facebook.com/", blank=True)
    
    def get_absolute_url(self):
        return "/users/%s" % self.owner.username

    def __str__(self):
        return "%s" % ( self.owner.username )
