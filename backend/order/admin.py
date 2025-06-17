from django.contrib import admin
from .models import Order, OrderItem
from products.models import Product  # 如果需要在 admin 中引用商品名等字段


admin.site.register(Order)
admin.site.register(OrderItem)