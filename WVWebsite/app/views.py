from django.shortcuts import render
from WVWebsite.app.models import Entry
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


def render_page(request):
    website = Entry.objects.all()
    return render(request, "index.html", {"Entries": website})

