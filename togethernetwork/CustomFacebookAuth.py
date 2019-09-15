from social_core.backends.facebook import FacebookOAuth2

class CustomFacebookOauth(FacebookOAuth2):
    REDIRECT_STATE = False