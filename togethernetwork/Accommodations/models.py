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

from datetime import datetime, timedelta

ACCOMMODATION_TYPE = [
    ('MOR', '4+ beds'),
    ('QUD', '4 beds'),
    ('TRP', '3 beds'),
    ('DOU', '2 beds'),
    ('SNG', '1 bed'),
]

BOOKING_STATUSES = [
    ('ACC', 'Accepted'),
    ('WFA', 'Waiting for approval'),
    ('WFP', 'Waiting for payment'),
    ('DEC', 'Declined'),
]

def get_accommodations_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("accommodations", filename)

class Accommodation(models.Model):
    """
        A single Accommodation.
    """
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500, default="")
    accommodation_type = models.CharField(max_length=3, choices=ACCOMMODATION_TYPE)
    photo = models.ImageField(upload_to=get_accommodations_path, blank=True, null=True)

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
        super(Accommodation, self).save()

    def get_absolute_url(self):
        return "/accommodations/%s" % self.pk

    def __str__(self):
        return "%s" % self.title

class Booking(models.Model):
    """
        The Booking for a period of time owned by a user for a specific Accommodation.
    """
    start = models.DateField(default=( datetime.now() + timedelta(days=1) ) )
    stop = models.DateField(default=( datetime.now() + timedelta(days=2) ) )

    status = models.CharField(max_length=3, choices=BOOKING_STATUSES)
    tenant = models.ForeignKey(User, related_name="booking_tenant")
    accommodation = models.ForeignKey(Accommodation, related_name="booking_accommodation")

    def get_absolute_url(self):
        return "/accommodations/%s/booking/%s" % ( self.accommodation.pk, self.pk )

    def __str__(self):
        return "(%s)[%s] %s booked by %s" % ( 
                self.start,
                self.status,
                self.accommodation.title, 
                self.tenant.username 
            )