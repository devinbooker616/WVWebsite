from django.contrib import admin
from WVWebsite.app.models import Post, About, WhiteListedEmail


class PostAdmin(admin.ModelAdmin):
    pass


class AboutAdmin(admin.ModelAdmin):
    pass


class WhiteListedEmailAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(WhiteListedEmail, WhiteListedEmailAdmin)
