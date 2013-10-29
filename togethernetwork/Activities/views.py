# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Activity

from .forms import ActivityForm

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

#@login_required
def new_activity_view(request, activity_pk=None):
    """
        Create a new activity
    """
    activity = None
    form_title = "New Activity"
    if activity_pk:
        form_title = "Edit Activity"
        activity = get_object_or_404(Activity, pk=activity_pk)

    if request.method == 'POST':
        formset = ActivityForm(request.POST, request.FILES, instance=None)
        if formset.is_valid():
            activity_obj = formset.save(commit=False)
            
            activity_obj.owner = request.user
            activity_obj.save()
            return redirect(teas_list)
    else:
        formset = ActivityForm(instance=None)
        
    return render_to_response("form.html", {
        "form": formset,
        "title": form_title
    }, context_instance=RequestContext(request))


