from django.contrib import admin
from WVWebsite.app.models import Entry


class EntryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Entry, EntryAdmin)
