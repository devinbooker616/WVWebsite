from django import forms


class EntryForm(forms.Form):
    textbox = forms.CharField()
