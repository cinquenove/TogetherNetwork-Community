# -*- coding=utf-8 -*-
import os
from PIL import Image
from cStringIO import StringIO

from datetime import datetime
import uuid

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template.defaultfilters import slugify

from datetime import datetime, timedelta

ACTIVITIES_TYPE = [
    ('TOU', 'Tourism/Territory'),
    ('CLA', 'Classes/Workshop'),
    ('EVN', 'Event/Party'),
]

def get_activity_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("Activities", filename)

class Location(models.Model):
    """
        A location where any activity can take place.
    """
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=256)

    def __str__(self):
        return "%s - %s" % ( self.title, self.address[:25] )

class Activity(models.Model):
    """
        A single Activity.

    """
    owner = models.ForeignKey(User, related_name="activity_author")
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500, default="", null=True, blank=True)
    activity_type = models.CharField(max_length=3, choices=ACTIVITIES_TYPE)

    time = models.DateTimeField(default=( datetime.now() + timedelta(days=1) ) )
    #TODO: if 0 is infinite.

    location = models.ForeignKey(Location, related_name="activity_location")
    photo = models.ImageField(upload_to=get_activity_path, blank=True, null=True)

    attendees_limit = models.IntegerField(default=0) 
    attendees = models.ManyToManyField(User, blank=True, null=True)
    price = models.FloatField(default=0.0) 

    def create_thumbnails(self):
        # original code for this method came from
        # http://snipt.net/danfreak/generate-thumbnails-in-django-with-pil/

        # If there is no image associated with this.
        # do not create thumbnail
        if not self.photo:
            return

        # Set our max thumbnail size in a tuple (max width, max height)
        THUMBNAIL_BIG_SIZE = (1200,1200)

        DJANGO_TYPE = self.photo.file.name.split("/")[-1].split(".")[-1].lower()
        if DJANGO_TYPE in ['jpeg', 'jpg']:
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE in ['png']:
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'

        # Open original photo which we want to thumbnail using PIL's Image
        file_read = self.photo.read()
        image_big = Image.open(StringIO(file_read))

        # Convert to RGB if necessary
        # Thanks to Limodou on DjangoSnippets.org
        # http://www.djangosnippets.org/snippets/20/
        #
        # I commented this part since it messes up my png files
        #
        #if image.mode not in ('L', 'RGB'):
        #    image = image.convert('RGB')

        # We use our PIL Image object to create the thumbnail, which already
        # has a thumbnail() convenience method that contrains proportions.
        # Additionally, we use Image.ANTIALIAS to make the image look better.
        # Without antialiasing the image pattern artifacts may result.
        image_big.thumbnail(THUMBNAIL_BIG_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
        temp_handle_big = StringIO()
        image_big.save(temp_handle_big, PIL_TYPE)
        temp_handle_big.seek(0)

        # Save image to a SimpleUploadedFile which can be saved into
        # ImageField
        suf_big = SimpleUploadedFile(os.path.split(self.photo.name)[-1],
             temp_handle_big.read(), content_type=DJANGO_TYPE)
        
        # Save SimpleUploadedFile into image field
        self.photo.save('%s_big.%s'%(os.path.splitext(suf_big.name)[0],FILE_EXTENSION), suf_big, save=False)
        
    def save(self):
        # create a thumbnail
        self.create_thumbnails()
        super(Activity, self).save()

    def get_absolute_url(self):
        return "/activities/%s/%s" % (self.pk, slugify(self.title))

    def __str__(self):
        return "( %s ) %s by %s " % ( self.time, self.title, self.owner.username )

class Comment(models.Model):
    """
        A single Activity Comment.

    """
    owner = models.ForeignKey(User, related_name="comment_owner")
    activity = models.ForeignKey(Activity, related_name="comment_activity")
    content = models.TextField(max_length=500, default="")
    pub_date = models.DateTimeField(default=datetime.now())

    def get_absolute_url(self):
        return "/activities/%s/%s#comment-%s" % (self.activity.pk, slugify(self.title), self.pk)

    def __str__(self):
        return "( %s ) %s by %s " % ( self.pub_date, self.activity.title, self.owner.username )



