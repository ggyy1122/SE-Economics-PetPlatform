
# Create your models here.
from django.db import models
from person.models import Person  #
from products.models import Product  # 假设你收藏的是产品

class Favorite(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE)  # 用户外键
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # 商品外键
    created_at = models.DateTimeField(auto_now_add=True)  # 收藏时间
    class Meta:
        unique_together = ('user', 'product')  # 确保一个用户只能收藏一次同一商品

    def __str__(self):
        return f"{self.user.name} favorites {self.product.name}"
