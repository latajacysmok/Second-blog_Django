from django.contrib import admin

from posts.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "update", "timestamp"]
    list_display_links = ["timestamp"]
    list_filter = ["title", "update", "timestamp"]
    list_editable = ["title"]
    search_fields = ["title"]
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)

