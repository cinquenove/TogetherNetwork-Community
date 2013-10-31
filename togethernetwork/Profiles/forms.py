# -*- coding=utf-8 -*-
from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            #"owner",
            "city",
            "mission",
            "bio",
            "interests_and_skilss",
            "personal_website_url",
            "twitter_url",
            "facebook_url",
        ]