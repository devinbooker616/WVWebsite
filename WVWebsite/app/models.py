from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Website(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    textbox = HTMLField()
