from django.contrib import admin
from .models import PostComment

@admin.register(PostComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'text', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__name', 'post__title', 'text')
