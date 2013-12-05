# -*- coding=utf-8 -*-
from django.contrib import admin 
from .models import Location
from .models import Activity
from .models import Comment

admin.site.register(Location)
admin.site.register(Activity)
admin.site.register(Comment)

