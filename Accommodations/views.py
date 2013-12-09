# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail, mail_admins

from django.contrib.auth.models import User

from .models import Accommodation
from .models import AccommodationPhoto
from .models import Booking
from .models import is_accommodation_available_for_booking
from .models import BOOKING_STATUSES

from .forms import BookingForm

from datetime import datetime, timedelta

def accommodations_view(request):
    """
        List of accommodations.
    """

    accommodations = Accommodation.objects.all()
    return render_to_response("accommodations.html", 
        {"accommodations": accommodations},
        context_instance=RequestContext(request))

def single_accommodation_view(request, accommodation_pk):
    """
        Show the single accommodation view
    """
    accommodation = get_object_or_404(Accommodation, pk=accommodation_pk)
    photos = AccommodationPhoto.objects.filter(accommodation=accommodation)
    bookings = Booking.objects.filter( 
                                        accommodation=accommodation, 
                                        checkin_date__gte=(datetime.now()-timedelta(days=(31*6))) 
                                    )
    return render_to_response("accommodation.html", 
        { "accommodation": accommodation, "photos": photos, "bookings": bookings }, 
        context_instance=RequestContext(request))


@login_required
def create_new_book_for_accommodation(request, accommodation_pk):
    """
        Create a new book for a single accommodation.
    """
    accommodation = get_object_or_404(Accommodation, pk=accommodation_pk)
    if accommodation.external_booking_url:
        return redirect(accommodation.external_booking_url)
    
    if request.method == 'POST':
        formset = BookingForm(request.POST, request.FILES)
        if formset.is_valid():
            booking_obj = formset.save(commit=False)
            booking_obj.accommodation = accommodation

            if not is_accommodation_available_for_booking(booking_obj):
                messages.error(request, 'Booking not available for specified dates')
                return render_to_response("form.html", {
                        "form": formset,
                        "title": "Make a reservation"
                    }, context_instance=RequestContext(request))

            # Calculating the right pice:
            delta_days = booking_obj.checkout_date - booking_obj.checkin_date
            spent_days = delta_days.days
            if spent_days <= 30:
                booking_obj.price = accommodation.price_per_month * spent_days
            else:
                booking_obj.price = accommodation.price_per_day * spent_days
            
            #TODO: send an email to ERNESTO!
            
            booking_obj.tenant = request.user
            booking_obj.save()
            mail_admins(
                "[Together] New Booking Order", 
                """New activity created by %s: 
http://www.togethernetwork.org%s

koala""" % (booking_obj.tenant.username, booking_obj.get_absolute_url()  ) )
            
            return redirect("%s/saved" % booking_obj.get_absolute_url() )
    else:
        formset = BookingForm()
        
    return render_to_response("form.html", {
        "form": formset,
        "title": "Make a reservation"
    }, context_instance=RequestContext(request))

@login_required
def single_booking_view(request, accommodation_pk, booking_pk):
    """
        This view will show the single booking view.
    """
    booking = get_object_or_404(Booking, pk=booking_pk)
    return render_to_response("booking.html", 
        { "booking": booking, "BOOKING_STATUSES": BOOKING_STATUSES }, 
        context_instance=RequestContext(request))


@login_required
def single_booking_confirmation_view(request, accommodation_pk, booking_pk):
    """
        This view will show the single booking confirmation.
    """
    booking = get_object_or_404(Booking, pk=booking_pk)
    return render_to_response("booking_done.html", 
        { "booking": booking, "BOOKING_STATUSES": BOOKING_STATUSES }, 
        context_instance=RequestContext(request))

