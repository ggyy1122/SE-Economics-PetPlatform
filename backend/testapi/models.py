

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)  # 商品名称
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 商品价格

    def __str__(self):
        return self.name
