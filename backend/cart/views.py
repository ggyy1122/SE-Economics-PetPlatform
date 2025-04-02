# cart/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Cart, CartItem
from products.models import Product
from person.models import Person
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cart, CartItem
from person.models import Person


# 获取指定用户的购物车数据（假设 userabcd 登录）
def get_user_cart(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return JsonResponse({'error': '用户未登录'}, status=401)

    user = get_object_or_404(Person, id=user_id)  # 获取当前用户
    cart, _ = Cart.objects.get_or_create(user=user)
    cart_items = cart.items.all()

    cart_data = [{
        'product_id': item.product.id,
        'product': item.product.name,
        'quantity': item.quantity,
        'total_price': item.total_price()
    } for item in cart_items]

    return JsonResponse({
        'user': user.name,
        'cart': cart_data,
        'total_price': cart.total_price()
    })


# 获取所有用户的购物车数据
def get_all_carts(request):
    carts = Cart.objects.all()
    data = []

    for cart in carts:
        user = cart.user
        cart_items = cart.items.all()

        cart_data = [{
            'product_id': item.product.id,
            'product': item.product.name,
            'quantity': item.quantity,
            'total_price': item.total_price()
        } for item in cart_items]

        data.append({
            'user': user.name,
            'cart': cart_data,
            'total_price': cart.total_price()
        })

    return JsonResponse({'carts': data})


@api_view(["POST"])
def add_to_cart(request, product_id):
    """添加商品到购物车"""
    user_id = request.session.get("user_id")
    if not user_id:
        return JsonResponse({'error': '用户未登录'}, status=401)

    user = get_object_or_404(Person, id=user_id)  # 获取当前用户
    product = get_object_or_404(Product, id=product_id)

    cart, _ = Cart.objects.get_or_create(user=user)

    # 查找购物车中是否已有该商品
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1  # 如果已存在，增加数量
    else:
        cart_item.quantity = 1  # 新增商品，数量为 1
    cart_item.save()

    return JsonResponse({
        'message': '商品已加入购物车',
        'product': product.name,
        'quantity': cart_item.quantity
    })


@api_view(["POST"])
def update_cart_item(request, product_id):
    """更新购物车中商品的数量"""
    user_id = request.session.get("user_id")
    if not user_id:
        return JsonResponse({'error': '用户未登录'}, status=401)

    user = get_object_or_404(Person, id=user_id)  # 当前用户
    product = get_object_or_404(Product, id=product_id)
    cart = get_object_or_404(Cart, user=user)

    cart_item = get_object_or_404(CartItem, cart=cart, product=product)

    new_quantity = request.data.get('quantity')
    if new_quantity is not None and int(new_quantity) > 0:
        cart_item.quantity = int(new_quantity)
        cart_item.save()
        return JsonResponse({
            'message': '购物车商品数量更新成功',
            'product': product.name,
            'quantity': cart_item.quantity
        })

    return JsonResponse({'error': '无效的商品数量'}, status=400)


@api_view(["POST"])
def remove_from_cart(request, product_id):
    """从购物车移除商品"""
    user_id = request.session.get("user_id")
    if not user_id:
        return JsonResponse({'error': '用户未登录'}, status=401)

    user = get_object_or_404(Person, id=user_id)
    product = get_object_or_404(Product, id=product_id)

    cart = get_object_or_404(Cart, user=user)

    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
    except CartItem.DoesNotExist:
        return JsonResponse({'message': '购物车中无此商品'}, status=404)

    # 数量大于1，减少数量，否则删除商品
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
        return JsonResponse({
            'message': '商品数量已减少',
            'product': product.name,
            'quantity': cart_item.quantity
        })
    else:
        cart_item.delete()
        return JsonResponse({
            'message': '商品已从购物车移除',
            'product': product.name
        })
