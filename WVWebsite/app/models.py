from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Home")


class About(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.TextField()

    def __str__(self):
        return self.content
