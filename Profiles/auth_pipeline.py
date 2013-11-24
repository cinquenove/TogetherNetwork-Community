from social_auth.backends.facebook import FacebookBackend
from .models import Profile

def get_user_avatar(backend, details, response, social_user, uid,\
                    user, *args, **kwargs):
    url = None
    if backend.__class__ == FacebookBackend:
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id'] 
    if url:
        try:
            the_profile = Profile.objects.get(user=user)
        except:
            the_profile = Profile()
            the_profile.user = user
        the_profile.first_name = user.first_name
        the_profile.last_name = user.last_name
        the_profile.email = user.email
        the_profile.avatar_url = url
        the_profile.save()