from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from .app.models import WhiteListedEmail


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_open_for_signup(self, request, socialaccount):
        emails = [w.email for w in WhiteListedEmail.objects.all()]
        return socialaccount.email in emails
