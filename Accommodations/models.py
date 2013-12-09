# -*- coding=utf-8 -*-
import os
from PIL import Image
from cStringIO import StringIO

from datetime import datetime
import uuid

from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

from datetime import datetime, timedelta

ROOM_SIZES = [
    ('FPD', '4 persons dorm'),
    ('DOU', 'Double'),
    ('SNG', 'Single'),
]

ROOM_TYPES = [
    ('LCL', 'Monthly'),
    ('GST', 'Nightly'),
    ('ALL', 'Monthly and Nightly'),
]

def get_accommodations_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("Accommodations", "main_photo", filename)

class Accommodation(models.Model):
    """
        A single Accommodation.
    """
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500, default="")
    room_size = models.CharField(max_length=3, choices=ROOM_SIZES)
    room_type = models.CharField(max_length=3, choices=ROOM_TYPES)
    main_photo = models.ImageField(upload_to=get_accommodations_path, blank=True, null=True)

    external_booking_url = models.URLField(blank=True, null=True)
    price_per_day = models.FloatField(default=0.0) 
    price_per_month = models.FloatField(default=0.0) 

    def create_thumbnails(self):
        if not self.main_photo:
            return

        THUMBNAIL_BIG_SIZE = (1200,1200)

        DJANGO_TYPE = self.main_photo.file.name.split("/")[-1].split(".")[-1].lower()
        if DJANGO_TYPE in ['jpeg', 'jpg']:
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif DJANGO_TYPE in ['png']:
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'

        file_read = self.main_photo.read()
        image_big = Image.open(StringIO(file_read))
        image_big.thumbnail(THUMBNAIL_BIG_SIZE, Image.ANTIALIAS)

        # Save the thumbnail
        temp_handle_big = StringIO()
        image_big.save(temp_handle_big, PIL_TYPE)
        temp_handle_big.seek(0)

        # Save image to a SimpleUploadedFile which can be saved into
        # ImageField
        suf_big = SimpleUploadedFile(os.path.split(self.main_photo.name)[-1],
             temp_handle_big.read(), content_type=DJANGO_TYPE)
        
        # Save SimpleUploadedFile into image field
        self.main_photo.save('%s_big.%s'%(os.path.splitext(suf_big.name)[0],FILE_EXTENSION), suf_big, save=False)
        
    def save(self):
        # create a thumbnail
        self.create_thumbnails()
        super(Accommodation, self).save()

    def get_absolute_url(self):
        return "/accommodations/%s" % self.pk

    def __str__(self):
        return "%s" % self.name

## AccommodationPhoto

def get_accommodation_photos_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("Accommodations", "photos", filename)

class AccommodationPhoto(models.Model):
    """
        A single Photo of a single Accommodation.
    """
    title = models.CharField(max_length=140, blank=True, default="")
    photo = models.ImageField(upload_to=get_accommodation_photos_path, blank=True, null=True)
    accommodation = models.ForeignKey(Accommodation, related_name="booking_accommodation")

    def create_thumbnails(self):
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
        if AccommodationPhoto.objects.filter(accommodation=self.accommodation).count() >= 4:
            raise Exception("Too many Photos! Delete one! ( max 4 photos per Accommodation )")
            return None
        # create a thumbnail
        self.create_thumbnails()
        super(AccommodationPhoto, self).save()

    def __str__(self):
        return "%s - %s %s" % (self.accommodation.name, self.pk, self.title)

## Booking 

BOOKING_STATUSES = [
    ('ACC', 'Accepted'),
    ('WFA', 'Waiting for approval'),
    ('WFP', 'Waiting for payment'),
    ('DEC', 'Declined'),
]

class Booking(models.Model):
    """
        The Booking for a period of time "owned" by a user for a specific Accommodation.
    """
    checkin_date = models.DateField(default=( datetime.now() + timedelta(days=1) ) )
    checkout_date = models.DateField(default=( datetime.now() + timedelta(days=2) ) )

    status = models.CharField(max_length=3, default="WFA", choices=BOOKING_STATUSES)
    tenant = models.ForeignKey(User, related_name="booking_tenant")
    accommodation = models.ForeignKey(Accommodation, related_name="booking_of_accommodation")
    price = models.FloatField(default=0.0) 

    def get_absolute_url(self):
        return "/accommodations/%s/booking/%s" % ( self.accommodation.pk, self.pk )

    def __str__(self):
        return "(%s)[%s] %s booked by %s" % ( 
                self.checkin_date,
                self.status,
                self.accommodation.name, 
                self.tenant.username 
            )

def is_accommodation_available_for_booking(booking):
    """
        This function check if an accommodation is available 
        for a specific time by checking if there are other booking in the specified period.
    """

    bookings = Booking.objects.filter( 
                                        Q( # Checkout dopo il checkin del booking
                                            accommodation=booking.accommodation,
                                            status="ACC",
                                            checkout_date__gte=booking.checkin_date,
                                            checkout_date__lte=booking.checkout_date
                                        ) | Q( # Interno
                                            accommodation=booking.accommodation,
                                            status="ACC",
                                            checkin_date__gte=booking.checkin_date,
                                            checkout_date__lte=booking.checkout_date
                                        ) | Q( # Checkin prima del checkout del booking
                                            accommodation=booking.accommodation,
                                            status="ACC",
                                            checkin_date__gte=booking.checkin_date,
                                            checkin_date__lte=booking.checkout_date
                                        ) | Q( # Esterno 
                                            accommodation=booking.accommodation,
                                            status="ACC",
                                            checkin_date__lte=booking.checkin_date,
                                            checkout_date__gte=booking.checkout_date
                                        )
                                    )
    if bookings:
        return False
    else:
        return True
