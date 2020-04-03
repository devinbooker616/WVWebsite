from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    textbox = HTMLField()
