# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404

from .models import Activity

def activities_view(request):
    """
        List of activities.
    """
    activities = Activity.objects.all()
    return render_to_response("activities.html", 
        {"activities": activities }, 
        context_instance=RequestContext(request))

def single_activity_view(request, activity_pk):
    """
        Show the single Activity view
    """
    activity = get_object_or_404(Activity, pk=activity_pk)
    return render_to_response("activity.html", 
        {"activity": activity }, 
        context_instance=RequestContext(request))



