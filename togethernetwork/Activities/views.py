# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Activity

def activities_view(request):
    """
        List of activities.
    """
    activities = Activity.objects.all()
    return render_to_response("activities.html", {"activities": activities }, context_instance=RequestContext(request))



