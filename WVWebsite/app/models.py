from django.db import models
from django.contrib.auth.models import User


class Website(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    textbox = models.TextField()
