# -*- coding=utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from Activities.models import Activity

from .models import Profile
from .forms import ProfileForm

def profile_view(request, username):
    """
        Show a single profile
    """
    try:
        profile = Profile.objects.get(owner__username=username)
    except:
        if username == request.user.username:
            return redirect(edit_profile_view)
        else:
            raise Http404

    return render_to_response("profile.html", 
        {"profile": profile }, 
        context_instance=RequestContext(request))

@login_required
def edit_profile_view(request):
    """
        Edit the Profile
    """
    form_title = "My Profile"

    try:
        profile = Profile.objects.get(owner=request.user)
    except:
        profile = Profile()

    if request.method == 'POST':
        formset = ProfileForm(request.POST, request.FILES, instance=profile)
        if formset.is_valid():
            profile_obj = formset.save(commit=False)
            
            profile_obj.owner = request.user

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
