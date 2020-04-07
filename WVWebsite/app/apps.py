from django.apps import AppConfig


class AppConfig(AppConfig):
    name = "WVWebsite.app"

    def ready(self):
        from . import checks

        return super().ready()
