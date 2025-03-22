from django.contrib import admin
from .models import Favorite

class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'created_at')  # 让 ID 也显示出来
    search_fields = ('user__name', 'product__name')  # 添加搜索功能，使用 user.name
    list_filter = ('created_at',)  # 让 admin 界面能按时间筛选

admin.site.register(Favorite, FavoriteAdmin)

