from django.contrib import admin
from WVWebsite.app.models import Post, About


class PostAdmin(admin.ModelAdmin):
    pass


class AboutAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(About, AboutAdmin)
