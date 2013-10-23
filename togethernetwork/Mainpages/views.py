# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response

from django.template import RequestContext

def homepage_view(request):
    """
        Static Homepage view.
    """

    return render_to_response("homepage.html", context_instance=RequestContext(request))

# Pillows actions# Create your views here.
