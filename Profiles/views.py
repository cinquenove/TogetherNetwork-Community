# -*- coding=utf-8 -*-
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
# from django.template import RequestContext
# from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
# from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView



# from datetime import datetime
from datetime import date

from django.contrib.auth.models import User
from Activities.models import Activity
from Accommodations.models import Booking

from .models import Profile
from .forms import ProfileForm, SearchCommunity

from django.db.models import Q

def homepage_view(request):
    """
        Show faces.
    """
    if request.user.is_authenticated():
        return redirect("/activities/list")
    profiles = Profile.objects.all().order_by("?")[:24]
    return render(request, template_name="homepage.html", context={"profiles": profiles})


def community_view(request):
    """
        List of profiles.
    """
    template="community.html"
    page_template="community_index_page.html"
    page = request.GET.get('page')
    name = request.GET.get('search')
    if name is None:
        name=""
        profiles = Profile.objects.all().order_by("?")
    else:
        profiles = Profile.objects.filter(Q(first_name__istartswith=name) | Q(last_name__istartswith=name)).order_by("?")
    paginator = Paginator(profiles, 24)
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        profiles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        profiles = []
    if request.is_ajax():
        template = page_template
    return render(request, template_name=template, context={'search': name,
                                                            "profiles": profiles,
                                                            "page_template": page_template,})



@login_required
def profile_view(request, username):
    """
        Show a single profile
    """
    try:
        profile = Profile.objects.get(user__username=username)
    except Exception as e:
        if username == request.user.username:
            return redirect(edit_profile_view)
        else:
            raise Http404

    partecipated_in_counter = Activity.objects.filter(
        attendees__in=[profile.user]).count()
    offered_counter = Activity.objects.filter(owner=profile.user).count()

    # user_status calculation
    user_status = "Never been"
    today = date.today()
    user_bookings = Booking.objects.filter(
        tenant=profile.user).order_by('-checkin_date')[:10]
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

    return render(request, template_name="profile.html", context={
                                  "profile": profile,
                                  "partecipated_in_counter": partecipated_in_counter,
                                  "offered_counter": offered_counter,
                                  "user_status": user_status
                              })
#        context_instance=RequestContext(request))


@login_required
def edit_profile_view(request):
    """
        Edit the Profile
    """
    form_title = "My Profile"

    try:
        profile = Profile.objects.get(user=request.user)
    except Exception as e:
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

    return render(request, template_name="form.html", context={
        "form": formset,
        "title": form_title})
#    }, context_instance=RequestContext(request))


@login_required
def text_email_addresses(request):
    """
        Returns a list of users email addresses divided by space
    """
    if not request.user.is_superuser:
        raise Http404

    emails = list()
    for user in User.objects.all():
        if user.email not in emails:
            emails.append(user.email)

    return HttpResponse(" ".join(emails))
