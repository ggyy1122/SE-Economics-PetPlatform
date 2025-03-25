from django.db import models
#2025-3-22 购物车相关两张表
# cart/models.py
from django.db import models
from person.models import Person
from products.models import Product

# 购物车模型
class Cart(models.Model):
    user = models.OneToOneField(Person, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.name} 的购物车"

    def total_price(self):
        """计算购物车总价"""
        return sum(item.total_price() for item in self.items.all())

# 购物车项模型
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product')

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def total_price(self):
        """计算该商品总价"""
        return self.product.price * self.quantity
