# -*- coding=utf-8 -*-
from django.http import Http404
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.template import RequestContext
from django.contrib import messages

from django.contrib.auth.models import User

from .models import Activity

from datetime import datetime, timedelta
import time

def home(request):
    """
        
    """
    activities = list()

    return render_to_response("derivato.html", 
        { "activities": activities }, 
        context_instance=RequestContext(request))

# Pillows actions