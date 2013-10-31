# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User



def accommodations_view(request):
    """
        List of activities.
    """

#    accommodations = Accommodation.objects.all()
    return render_to_response("accommodations.html", 
        context_instance=RequestContext(request))

