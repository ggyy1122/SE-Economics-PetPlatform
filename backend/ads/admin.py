from django.contrib import admin

# Register your models here.
# ads/admin.py
from django.contrib import admin
from .models import Ad  # 确保正确导入 Ad 模型

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'location', 'created_at')  # 显示的字段
    ordering = ('-created_at',)  # 按时间排序
