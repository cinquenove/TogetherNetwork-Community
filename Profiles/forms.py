# -*- coding=utf-8 -*-
from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            #"user",
            "first_name",
            "last_name",
            "email",
            "city",
            "mission",
            "bio",
            "skills",
            "personal_website_url",
            "twitter_url",
            "facebook_url",
        ]