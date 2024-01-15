import sys
from django.apps import AppConfig


class Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'server_main'

    def ready(self):
        print("app config is working")
