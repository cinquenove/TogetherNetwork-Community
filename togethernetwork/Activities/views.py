# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response

from django.template import RequestContext

def activities_view(request):
    """
        List of activities.
    """
    return render_to_response("activities.html", context_instance=RequestContext(request))



