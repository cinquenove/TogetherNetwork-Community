# -*- coding=utf-8 -*-
from django.forms import ModelForm
from .models import Activity

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = [
            #"owner",
            "title",
            "description",
            "activity_type",

            "time",
            "location",
            "photo",

            "attendees_limit",
            #"attendees",
            "price",
        ]