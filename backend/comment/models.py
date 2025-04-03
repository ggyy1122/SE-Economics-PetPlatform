# 2025-4-3 评论区制作
from django.db import models
from products.models import Product  # 假设商品模型在 products 应用中
from person.models import Person  # 假设用户模型在 person 应用中

class Comment(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='comments')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    image = models.ImageField(upload_to='comments/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.name} on {self.product.name}"

    class Meta:
        ordering = ['-created_at']
from django.db import models

# Create your models here.
