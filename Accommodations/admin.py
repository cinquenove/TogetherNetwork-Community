# -*- coding=utf-8 -*-
from django.contrib import admin 
from .models import Accommodation
from .models import AccommodationPhoto
from .models import Booking

admin.site.register(Accommodation)
admin.site.register(AccommodationPhoto)
admin.site.register(Booking)

