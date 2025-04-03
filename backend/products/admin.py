from django.contrib import admin
from .models import Product, Animal, Category

# 动物和分类模型的注册
class AnimalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

# 产品模型的注册
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]  # 显示所有字段
    list_editable = [field.name for field in Product._meta.fields if field.name != "id"]  # 允许编辑所有非主键字段
    readonly_fields = ('id',)  # id 设为只读，防止修改
    filter_horizontal = ('animals', 'categories')  # 让 animals 和 categories 字段显示为横向选择框，便于多选

# 注册模型到 Admin
admin.site.register(Product, ProductAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Category, CategoryAdmin)
