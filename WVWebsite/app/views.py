from django.shortcuts import render
from WVWebsite.app.models import Entry


def render_page(request):
    website = Entry.objects.all()
    return render(request, "home.html", {"Entries": website})
