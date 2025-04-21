from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import F
from favorites.models import Favorite
from products.models import Product

@receiver(post_save, sender=Favorite)
def update_favorite_count_on_add(sender, instance, created, **kwargs):
    if created:  # 只有在创建新的收藏时更新
        product = instance.product
        product.favorite_count = F('favorite_count') + 1  # 使用 F 表达式进行原子性更新
        product.save()

@receiver(post_delete, sender=Favorite)
def update_favorite_count_on_delete(sender, instance, **kwargs):
    product = instance.product
    product.favorite_count = F('favorite_count') - 1  # 使用 F 表达式进行原子性更新
    product.save()
