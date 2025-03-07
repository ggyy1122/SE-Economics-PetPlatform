from django.http import JsonResponse
from .models import Product

def get_products(request):
    products = Product.objects.all()  # 获取所有商品
    products_data = []
    for product in products:
        products_data.append({
            'name': product.name,
            'price': str(product.price)  # 将价格转为字符串，避免浮点数精度问题
        })
    return JsonResponse({'products': products_data})