from django.contrib import admin
from WVWebsite.app.models import Comment, Post


class PostAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
