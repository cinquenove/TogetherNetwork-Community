# -*- coding=utf-8 -*-
from django.shortcuts import render_to_response

from django.template import RequestContext

def homepage_view(request):
    """
        Static Homepage view.
    """
    return render_to_response("homepage.html", context_instance=RequestContext(request))

def about_view(request):
    """
        Static About view.
    """
    return render_to_response("about.html", context_instance=RequestContext(request))
