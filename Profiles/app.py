from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'Profiles'
    verbose_name = 'Profiles'

    def ready(self):
        # import signal handlers
        import Profiles.signals
