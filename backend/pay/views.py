from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from order.models import Order
from alipay import AliPay
from django.conf import settings
import os
import json
import decimal
import traceback


@csrf_exempt
def create_payment(request):
    try:
        # 1. 解析请求数据（支持 JSON 和表单）
        if request.content_type == "application/json":
            data = json.loads(request.body.decode("utf-8"))
        else:
            data = request.POST

        out_trade_no = data.get("out_trade_no")
        if not out_trade_no:
            return JsonResponse({"error": "缺少订单号"}, status=400)

        # 2. 查询订单是否存在
        try:
            order = Order.objects.get(out_trade_no=out_trade_no)
        except Order.DoesNotExist:
            return JsonResponse({"error": "订单不存在"}, status=404)

        # 3. 读取订单金额与描述，金额转换为Decimal
        amount_dec = decimal.Decimal(order.amount)
        if amount_dec < decimal.Decimal("0.01"):
            return JsonResponse({"error": "订单金额不能小于0.01"}, status=400)
        subject = f"商品订单 {out_trade_no}"

        # 4. 验证密钥文件是否存在
        app_private_key_path = getattr(settings, 'ALIPAY_APP_PRIVATE_KEY_PATH', None)
        alipay_public_key_path = getattr(settings, 'ALIPAY_PUBLIC_KEY_PATH', None)

        if not all([
            app_private_key_path and os.path.exists(app_private_key_path),
            alipay_public_key_path and os.path.exists(alipay_public_key_path)
        ]):
            return JsonResponse({"error": "密钥文件不存在，请检查路径"}, status=500)

        # 5. 加载密钥文件内容，并strip去除多余空白
        with open(app_private_key_path, "r") as f:
            app_private_key = f.read().strip()

        with open(alipay_public_key_path, "r") as f:
            alipay_public_key = f.read().strip()

        # 6. 初始化支付宝 SDK
        alipay = AliPay(
            appid=getattr(settings, "ALIPAY_APPID", "2021000119683233"),
            app_notify_url="http://yourdomain.com/alipay/notify/",  # 建议写一个实际可访问的异步通知地址
            app_private_key_string=app_private_key,
            alipay_public_key_string=alipay_public_key,
            sign_type="RSA2",
            debug=True
        )

        # 7. 创建订单字符串，增加 product_code="FAST_INSTANT_TRADE_PAY" 明确交易类型（必需）
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=out_trade_no,
            total_amount=str(amount_dec),
            subject=subject,
            return_url="http://localhost:8080/",
            product_code="FAST_INSTANT_TRADE_PAY"
        )

        # 8. 沙箱环境使用 sandbox 地址，线上环境使用正式地址
        if getattr(settings, "ALIPAY_USE_SANDBOX", True):
            gateway = "https://openapi-sandbox.dl.alipaydev.com/gateway.do"
        else:
            gateway = "https://openapi.alipay.com/gateway.do"

        pay_url = f"{gateway}?{order_string}"

        # 9. 返回支付链接
        return JsonResponse({
            "pay_url": pay_url,
            "out_trade_no": out_trade_no,
            "amount": str(amount_dec),
            "subject": subject
        })

    except Exception as e:
        traceback.print_exc()
        return JsonResponse({"error": f"支付链接创建失败: {str(e)}"}, status=500)
