from django.shortcuts import render, redirect
from WVWebsite.app.models import Entry
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from WVWebsite.app.forms import EntryForm
from django import forms


def render_page(request):
    website = Entry.objects.all()
    return render(request, "index.html", {"Entries": website})


def new_post(request):
    forms = EntryForm(request.POST)
    if forms.is_valid():
        textbox = forms.cleaned_data["textbox"]
        new_entry = Entry.objects.create(textbox=textbox)
        return redirect("index")
