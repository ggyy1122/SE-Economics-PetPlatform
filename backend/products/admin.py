#2025/3/10 注册产品模型，便于admin管理
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]  # 显示所有字段
    list_editable = [field.name for field in Product._meta.fields if field.name != "id"]  # 允许编辑所有非主键字段
    readonly_fields = ('id',)  # id 设为只读，防止修改

admin.site.register(Product, ProductAdmin)
