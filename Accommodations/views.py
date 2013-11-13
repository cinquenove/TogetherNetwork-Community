# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.models import User

from .models import Accommodation
from .models import AccommodationPhoto

from .models import Booking
from .models import is_accommodation_available_for_booking
from .forms import BookingForm


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
    return render_to_response("accommodation.html", 
        { "accommodation": accommodation, "photos": photos }, 
        context_instance=RequestContext(request))


def create_new_book_for_accommodation(request, accommodation_pk):
    """
        Create a new book for a single accommodation.
    """
    accommodation = get_object_or_404(Accommodation, pk=accommodation_pk)
    
    if request.method == 'POST':
        formset = BookingForm(request.POST, request.FILES)
        if formset.is_valid():
            booking_obj = formset.save(commit=False)
            if not is_accommodation_available_for_booking(booking_obj):
                messages.error(request, 'Booking not available for specified dates')
                error=True
            #TODO: Set Price in base of the days sleeping.
            #TODO: send an email to ERNESTO!
            
            booking_obj.tenant = request.user
            booking_obj.accommodation = accommodation
            booking_obj.save()
            return redirect(booking_obj)
    else:
        formset = BookingForm()
        
    return render_to_response("form.html", {
        "form": formset,
        "title": "Make a reservation"
    }, context_instance=RequestContext(request))

def single_booking_view(request, accommodation_pk, booking_pk):
    """
        This view will show the single booking view.
    """
    booking = get_object_or_404(Booking, pk=booking_pk)
    return render_to_response("booking.html", 
        { "booking": booking }, 
        context_instance=RequestContext(request))

