from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "LHV_cust"

    def ready(self):
        import_module("LHV_cust.receivers")
