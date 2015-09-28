# -*- coding=utf-8 -*-
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from datetime import datetime
from datetime import date

from django.contrib.auth.models import User
from Activities.models import Activity
from Accommodations.models import Booking

from .models import Profile
from .forms import ProfileForm

def homepage_view(request):
    """
        Show faces.
    """
    if request.user.is_authenticated():
        return redirect("/activities/list")
    profiles = Profile.objects.all().order_by("?")[:24]
    return render_to_response("homepage.html", 
        {"profiles": profiles }, 
        context_instance=RequestContext(request))

def community_view(request):
    """
        List of profiles.
    """
    profiles = Profile.objects.all().order_by("?")
    return render_to_response("community.html", 
        {"profiles": profiles }, 
        context_instance=RequestContext(request))

@login_required
def profile_view(request, username):
    """
        Show a single profile
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except:
        if username == request.user.username:
            return redirect(edit_profile_view)
        else:
            raise Http404


    partecipated_in_counter = Activity.objects.filter(attendees__in=[profile.user]).count()
    offered_counter = Activity.objects.filter(owner=profile.user).count()

    #user_status calculation
    user_status = "Never been"
    today = date.today()
    user_bookings = Booking.objects.filter(tenant=profile.user).order_by('-checkin_date')[:10]
    for booking in user_bookings:
        # Current booking
        if booking.checkin_date <= today and booking.checkout_date >= today:
            user_status = "Living"
            break

        # Future Booking
        if booking.checkin_date <= today and booking.checkout_date <= today:
            user_status = "Will Live"
            break
        # Old Booking
        if booking.checkin_date <= today and booking.checkout_date <= today:
            user_status = "Lived"

    if user_status == "Never been":
        if partecipated_in_counter > 0:
            user_status = "Active user"
            
        if offered_counter > 0:
            user_status = "Active user"
        
    return render_to_response("profile.html", 
        { 
            "profile": profile,
            "partecipated_in_counter": partecipated_in_counter,
            "offered_counter": offered_counter,
            "user_status": user_status
        }, 
        context_instance=RequestContext(request))

@login_required
def edit_profile_view(request):
    """
        Edit the Profile
    """
    form_title = "My Profile"

    try:
        profile = Profile.objects.get(user=request.user)
    except:
        profile = Profile()

    if request.method == 'POST':
        formset = ProfileForm(request.POST, request.FILES, instance=profile)
        if formset.is_valid():
            profile_obj = formset.save(commit=False)
            
            profile_obj.user = request.user

            request.user.email = profile_obj.email
            request.user.first_name = profile_obj.first_name
            request.user.last_name = profile_obj.last_name
            request.user.save()

            profile_obj.save()
            return redirect(profile_obj)
    else:
        profile.email = request.user.email
        profile.first_name = request.user.first_name
        profile.last_name = request.user.last_name
        
        formset = ProfileForm(instance=profile)
        
    return render_to_response("form.html", {
        "form": formset,
        "title": form_title
    }, context_instance=RequestContext(request))

@login_required
def text_email_addresses(request):
    """
        Returns a list of users email addresses divided by space
    """
    if not request.user.is_superuser:
        raise Http404

    emails = list()
    for user in User.objects.all():
        if not user.email in emails:
            emails.append(user.email)

    return HttpResponse(" ".join(emails))