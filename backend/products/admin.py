#2025/3/10 注册产品模型，便于admin管理
from django.contrib import admin
from .models import Product

admin.site.register(Product)