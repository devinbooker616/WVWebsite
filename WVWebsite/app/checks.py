from django.conf import settings
from django.core.checks import Error, register


@register(deploy=True)
def production_doesnt_run_on_sqlite(*args, **kwargs):
    default_db = settings.DATABASES["default"]
    if default_db["ENGINE"] == "django.db.backends.sqlite3":
        return [
            Error(
                "Production shouldn't run on sqlite.",
                hint="The DATABASE_URL should be set to an appropriate value for production. Assuming this website is hosted on Heroku, you should set it in the app config vars.",
                id="app.E001",
            )
        ]
    return []
