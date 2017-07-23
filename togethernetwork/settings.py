# -*- coding=utf-8 -*-
# Django settings for togethernetwork project.

import os
# from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
import dj_database_url


DEBUG = True
# TEMPLATE_DEBUG = DEBUG
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..")

ADMINS = (
    # ('Lorenzo Setale', 'koalalorenzo@gmail.com'),
    ('Ernesto Palermini', 'ernestocinquenove@gmail.com'),
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'database.sql',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '', # Set to empty string for default.
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Rome'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-US'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "uploads/")
MEDIA_ROOT = "/media/"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = 'http://media.togethernetwork.org.s3.amazonaws.com/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
#STATIC_ROOT = os.path.join(BASE_DIR,"staticfiles")
STATIC_ROOT = ""

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
#STATIC_URL = 'http://static.togethernetwork.org.s3.amazonaws.com/'
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
DEFAULT_FILE_STORAGE = 'togethernetwork.s3utils.STATICFILES_STORAGE'


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'h5**$ezazj#p-d)c#ctnqs0^ozue(b0y6*dxz8j=#d%lj+*vdz'

# TEMPLATE_DIRS = (
#     # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
#     # Always use forward slashes, even on Windows.
#     # Don't forget to use absolute paths, not relative paths.
#     os.path.join(BASE_DIR, "templates"),
# )

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# # List of callables that know how to import templates from various sources.
# TEMPLATE_LOADERS = (
#     'django.template.loaders.filesystem.Loader',
#     'django.template.loaders.app_directories.Loader',
#     'django.contrib.auth.context_processors.auth',
#     'django.template.context_processors.debug',
#     'django.template.context_processors.i18n',
#     'django.template.context_processors.media',
#     'django.template.context_processors.static',
#     'django.template.context_processors.tz',
#     'django.contrib.messages.context_processors.messages',

# #     'django.template.loaders.eggs.Loader',
# )

# # TEMPLATE_CONTEXT_PROCESSORS = TCP + (
# #     'django.core.context_processors.request',
# #     'social_auth.context_processors.social_auth_by_name_backends',
# #     'social_auth.context_processors.social_auth_backends',
# #     'social_auth.context_processors.social_auth_by_type_backends',
# #     'social_auth.context_processors.social_auth_login_redirect',
# # )

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware'
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'togethernetwork.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'togethernetwork.wsgi.application'

AUTHENTICATION_BACKENDS = (
#    'social_auth.backends.facebook.FacebookBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    
)

AUTH_PROFILE_MODULE = 'Profiles.Profile'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'django.contrib.humanize',    
    # Community Components
    # 'social_auth', # deprecated
    'django_extensions',
    'storages',
    'registration',
    'dbdump',
    'social_django',
    'captcha',
    #'avatar',
    
    # Private Components
    "Activities",
    "Profiles",
    "Accommodations",

    # Migrations and Database Community Components
    # 'south',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Email
EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST= 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']

# Django Messages (integrated)
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# Django Registration
ACCOUNT_ACTIVATION_DAYS = 7

# Django Avatars
AVATAR_DEFAULT_SIZE = 120
AVATAR_HASH_FILENAMES = True
AVATAR_HASH_USERDIRNAMES = False
AVATAR_GRAVATAR_BACKUP = True

# Django Storages
#DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'
#DEFAULT_FILE_STORAGE = 'togethernetwork.s3utils.STATICFILES_STORAGE'
#STATICFILES_STORAGE = 'togethernetwork.s3utils.STATICFILES_STORAGE'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
#AWS_S3_CALLING_FORMAT='boto.s3.connection.OrdinaryCallingFormat'
S3_BUCKET = AWS_STORAGE_BUCKET_NAME
AWS_ACCESS_KEY = AWS_ACCESS_KEY_ID

AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# see http://developer.yahoo.com/performance/rules.html#expires
AWS_HEADERS = {
    'Cache-Control': 'max-age=86400',
    'Accept-Encoding': 'gzip, deflate',
    #'Content-Encoding': 'gzip'
}

#Django social auth
LOGIN_URL = "/accounts/login/"
LOGOUT_URL = 'logout'
LOGIN_REDRECT_URL = "/activities/list"


SOCIAL_AUTH_FACEBOOK_KEY = '605827832822869'
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('FACEBOOK_SECRET_KEY')
# FACEBOOK_EXTENDED_PERMISSIONS = ['email','user_about_me','user_birthday','user_hometown','user_location','publish_actions']
# FACEBOOK_PROFILE_EXTRA_PARAMS = {}

# FACEBOOK_API_ID = FACEBOOK_APP_ID
# FACEBOOK_API_SECRET = FACEBOOK_SECRET_KEY

SOCIAL_AUTH_NEW_USER_REDIRECT_URL = "/users/edit"
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/activities/list"
SOCIAL_AUTH_LOGIN_ERROR_URL = "/activities/list"
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.mail.mail_validation',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)

RECAPTCHA_PUBLIC_KEY = '6Ld3qxUTAAAAAJ3A1LhCQK-qHFAp0uQsxlTuBoTk'
RECAPTCHA_PRIVATE_KEY = '6Ld3qxUTAAAAAOV33yPi0wUJY2eb08XLE6e4-jip'
RECAPTCHA_USE_SSL = True
NOCAPTCHA = True

import mimetypes
mimetypes.add_type("text/css", ".css", True)

import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

