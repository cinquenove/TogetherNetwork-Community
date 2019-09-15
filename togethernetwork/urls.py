# -*- coding=utf-8 -*-
from django.conf.urls import include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.contrib.auth.views import logout
from Profiles.views import homepage_view
from registration.backends.default.views import RegistrationView
from Profiles.forms import RecaptchaRegistrationForm
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    # Django Components
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
    #     {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),

    # Community Developed Components
    # url(r'^accounts/register/$', RegistrationView.as_view(form_class=RecaptchaRegistrationForm),
    #     name='registration.views.register'),  # email disabled
    # email disabled
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^accounts/', include('registration.backends.default.urls')), # enable email
    #url(r'^avatar/', include('avatar.urls')),
    url(r'^logout$', logout, {'next_page': homepage_view}), # 'django.contrib.auth.views.logout', {'next_page': '/'}),

    # Custom Components
    url(r'^accommodations/', include('Accommodations.urls')),
    url(r'^users/', include('Profiles.urls')),
    url(r'^activities/', include('Activities.urls')),
    url('', include('social_django.urls', namespace='social')),
    url(r'^oauth', include('social_django.urls', namespace='social')),
    # Static Pages
    url(r'^principles$', TemplateView.as_view(
        template_name='static_pages/principles.html')),
    url(r'^about$', TemplateView.as_view(
        template_name='static_pages/about.html')),
    url(r'^where$', TemplateView.as_view(
        template_name='static_pages/where.html')),
    # url(r'', include('social_auth.urls')),
    url(r'', homepage_view, name='homepage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
