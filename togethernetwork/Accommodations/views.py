# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .models import Accommodation


def accommodations_view(request):
    """
        List of accommodations.
    """

    accommodations = Accommodation.objects.all()
    return render_to_response("accommodations.html", 
        {"accommodations": accommodations},
        context_instance=RequestContext(request))

def single_accommodation_view(request, accommodation_pk):
    """
        Show the single accommodation view
    """
    accommodation = get_object_or_404(Accommodation, pk=accommodation_pk)
    return render_to_response("accommodation.html", 
        {"accommodation": accommodation }, 
        context_instance=RequestContext(request))

