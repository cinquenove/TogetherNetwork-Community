# -*- coding=utf-8 -*-
from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = [
            "checkin_date",
            "checkout_date",
            #"status",
            #"tenant",
            #"accommodation",
        ]