# -*- coding=utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import uuid
import os
from datetime import datetime, timedelta

ACTIVITIES_TYPE = [
    ('TOU', 'Tourism/Territory'),
    ('CLA', 'Classes/Workshop'),
    ('EVN', 'Event/Party'),
]

def get_activity_photo_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("Activties","photos", filename)

class Activity(models.Model):
    """
        One Activity.
    """
    owner = models.ForeignKey(User, related_name="event_author")
    name = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(max_length=500)
    activity_type = models.CharField(max_length=3, choices=ACTIVITIES_TYPE)

    attendees = models.ManyToManyField(User) 
    
    start = models.DateTimeField(default=( datetime.now() + timedelta(days=1) ) )
    end = models.DateTimeField(default=( datetime.now() + timedelta(days=1, hours=1) ) )

    photo = models.ImageField(upload_to=get_activity_photo_path)

    def __str__(self):
        return "%s" % self.name 
