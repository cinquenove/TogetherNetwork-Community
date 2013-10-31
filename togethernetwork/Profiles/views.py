# -*- coding=utf-8 -*-
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
    profile = get_object_or_404(Profile, owner__username=username)

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
        profile = None

    if request.method == 'POST':
        formset = ProfileForm(request.POST, request.FILES, instance=profile)
        if formset.is_valid():
            profile_obj = formset.save(commit=False)
            
            profile_obj.owner = request.user
            profile_obj.save()
            return redirect(profile_obj)
    else:
        formset = ProfileForm(instance=profile)
        
    return render_to_response("form.html", {
        "form": formset,
        "title": form_title
    }, context_instance=RequestContext(request))
