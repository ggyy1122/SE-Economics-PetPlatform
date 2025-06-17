import uuid
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
from alipay import AliPay
from .models import Order, OrderItem, Person
from products.models import Product  # 假设商品模型在 product 应用


# 支付宝回调通知接口
@csrf_exempt
def alipay_notify(request):
    if request.method == "POST":
        data = request.POST.dict()
        signature = data.pop("sign")

        # 加载密钥
        with open(settings.ALIPAY_APP_PRIVATE_KEY_PATH) as f:
            private_key = f.read()

        with open(settings.ALIPAY_PUBLIC_KEY_PATH) as f:
            public_key = f.read()

        alipay = AliPay(
            appid=settings.ALIPAY_APPID,
            app_notify_url=None,
            app_private_key_string=private_key,
            alipay_public_key_string=public_key,
            sign_type="RSA2",
            debug=True
        )

        # 验证签名
        success = alipay.verify(data, signature)
        if success:
            order_no = data.get("out_trade_no")
            trade_status = data.get("trade_status")

            if trade_status in ["TRADE_SUCCESS", "TRADE_FINISHED"]:
                try:
                    order = Order.objects.get(out_trade_no=order_no)
                    order.status = "paid"
                    order.save()
                    return HttpResponse("success")
                except Order.DoesNotExist:
                    return HttpResponse("fail")

        return HttpResponse("fail")
    return HttpResponse("only POST allowed")


# 创建订单接口
@csrf_exempt
def create_order(request):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST allowed"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    user_id = request.session.get("user_id")
    if not user_id:
        return JsonResponse({"error": "用户未登录"}, status=401)

    user = get_object_or_404(Person, id=user_id)

    items = data.get("items", [])
    if not items:
        return JsonResponse({"error": "订单项不能为空"}, status=400)

    # 生成订单编号
    out_trade_no = "ORDER_" + uuid.uuid4().hex[:16].upper()

    order = Order.objects.create(
        user=user,
        out_trade_no=out_trade_no,
        amount=0.0,
        status="unpaid"
    )

    total_amount = 0.0
    for item in items:
        product_id = item.get("product_id")
        quantity = item.get("quantity", 1)
        product = get_object_or_404(Product, id=product_id)
        total_price = float(product.price) * quantity
        total_amount += total_price

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity
        )

    order.amount = total_amount
    order.save()

    return JsonResponse({
        "message": "订单创建成功",
        "out_trade_no": order.out_trade_no,
        "amount": float(order.amount)
    })


# 获取当前用户所有订单
def get_user_orders(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return JsonResponse({'error': '用户未登录'}, status=401)

    user = get_object_or_404(Person, id=user_id)
    orders = Order.objects.filter(user=user).order_by('-created_at')

    order_list = []
    for order in orders:
        items = order.items.all()
        item_list = [{
            'product_name': item.product.name,
            'quantity': item.quantity
        } for item in items]

        order_list.append({
            'out_trade_no': order.out_trade_no,
            'amount': float(order.amount),
            'status': order.status,
            'created_at': order.created_at.isoformat(),
            'items': item_list
        })

    return JsonResponse({
        'user': user.name,
        'orders': order_list,
        'order_count': len(order_list)
    })
