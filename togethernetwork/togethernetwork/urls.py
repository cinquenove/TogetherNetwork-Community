# -*- coding=utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic import RedirectView
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/', include('registration.backends.simple.urls')), # email disabled
    #url(r'^accounts/', include('registration.backends.default.urls')), # enable email
    url(r'^avatar/', include('avatar.urls')),

    url(r'^accommodations/', include('Accommodations.urls')),
    url(r'^users/', include('Profiles.urls')),
    url(r'^activities/', include('Activities.urls')),
    
    url(r'^about$', TemplateView.as_view(template_name='pages/about.html')),
    url(r'^$', TemplateView.as_view(template_name='pages/homepage.html')),
)