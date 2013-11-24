from social_auth.backends.facebook import FacebookBackend

def get_user_avatar(backend, details, response, social_user, uid,\
                    user, *args, **kwargs):
    url = None
    if backend.__class__ == FacebookBackend:
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id'] 
    if url:
        the_profile = Profile.objects.get(owner=user)
        if not the_profile:
            the_profile = Profile()
            the_profile.owner = user
        the_profile.first_name = user.first_name
        the_profile.last_name = user.last_name
        the_profile.email = user.email
        the_profile.avatar_url = the_avatar_url
        the_profile.save()