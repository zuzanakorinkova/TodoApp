from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    name = 'user_profile'

#  we must make sure that the signal is registered as soon as
# the WSGI server starts serving the project
# with ready method, we import create_user_profile
    def ready(self):
        from . signals import create_user_profile
