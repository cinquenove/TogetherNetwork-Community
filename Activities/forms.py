# -*- coding=utf-8 -*-
from django.forms import ModelForm
from .models import Activity
from .models import Comment

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

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            #"owner",
            "content"
            #"pub_date",
        ]