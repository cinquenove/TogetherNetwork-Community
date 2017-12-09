# -*- coding=utf-8 -*-
# import os
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid
import os

import hashlib

def get_user_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("Profiles", filename)

class Profile(models.Model):
    """
        Single User Profile
    """
    def get_absolute_url(self):
        return "/users/%s/" % self.user.username

    user = models.OneToOneField(User, unique=True, primary_key=True, related_name="profile")

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    avatar_url = models.URLField(default="", blank=True)

    # TODO: relation with space by checking other database models ( Bookins,
    # Activities ecc..)
    city = models.CharField(max_length=200, blank=True)
    bio = models.TextField(max_length=500, default="", blank=True)
    skills = models.TextField(max_length=500, default="", blank=True)
    mission = models.CharField(max_length=250, blank=True)
    photo = models.ImageField(upload_to=get_user_path, blank=True, null=True)


    personal_website_url = models.URLField(blank=True)
    twitter_url = models.URLField(default="http://twitter.com/", blank=True)
    facebook_url = models.URLField(default="http://facebook.com/", blank=True)

    def get_the_avatar_url(self):
        if self.photo:
            if self.photo.url:
                return self.photo.url
        if not self.avatar_url:
            self.avatar_url = "http://www.gravatar.com/avatar/" + \
                hashlib.md5(self.email.lower()).hexdigest() + "?s=300"
        return self.avatar_url


    def __str__(self):
        return "%s" % (self.user.username)


