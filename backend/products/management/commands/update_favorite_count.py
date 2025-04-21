from django.core.management.base import BaseCommand
from products.models import Product
from favorites.models import Favorite  # 修改为正确的应用名
from django.db.models import Count

class Command(BaseCommand):
    help = "同步每个商品被收藏的人数到 favorite_count 字段"

    def handle(self, *args, **options):
        # 把所有商品收藏数清零（防止残留旧数据）
        Product.objects.update(favorite_count=0)

        # 聚合统计收藏数
        favorite_data = Favorite.objects.values('product').annotate(count=Count('user'))

        updated = 0
        for entry in favorite_data:
            product_id = entry['product']
            count = entry['count']
            Product.objects.filter(id=product_id).update(favorite_count=count)
            updated += 1

        self.stdout.write(self.style.SUCCESS(f"✅ 更新完成，共更新 {updated} 个商品的收藏数。"))
