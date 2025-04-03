from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'text', 'created_at')  # 显示的字段
    search_fields = ('user__name', 'product__name', 'text')  # 可搜索的字段
    list_filter = ('created_at', 'product')  # 可过滤的字段
    ordering = ('-created_at',)  # 默认排序方式

admin.site.register(Comment, CommentAdmin)

