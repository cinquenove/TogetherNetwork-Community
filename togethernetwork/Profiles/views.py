# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from Activities.models import Activity

from .models import Profile

def profile_view(request, profile_pk=None):
    """
        Show a single profile
    """
    profile = None
    if profile_pk:
        profile = get_object_or_404(Profile, pk=profile_pk)

    return render_to_response("profile.html", 
        {"profile": profile }, 
        context_instance=RequestContext(request))