from django.contrib import admin
from post.models import Post
from post.models import Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['-id']
    search_fields = ['name']
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
