#2025/3/10 产品模型
from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)  # 显式声明 id 作为主键
    name = models.CharField(max_length=255)
    description = models.TextField()
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)


    def __str__(self):
        return self.name