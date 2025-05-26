from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from alipay import AliPay
import os
import time
import decimal  # 用于金额验证


@csrf_exempt
def create_payment(request):
    """
    支持动态金额的支付宝支付接口
    请求参数：
    - amount: 支付金额（必须，最小0.01元）
    - subject: 商品描述（可选，默认"测试支付"）
    """
    # 1. 验证密钥文件
    if not all([
        os.path.exists(settings.ALIPAY_APP_PRIVATE_KEY_PATH),
        os.path.exists(settings.ALIPAY_PUBLIC_KEY_PATH)
    ]):
        return JsonResponse({"error": "密钥文件不存在"}, status=500)

    # 2. 获取请求参数（支持GET和POST）
    amount = request.GET.get('amount') or request.POST.get('amount')  # 优先GET参数
    subject = request.GET.get('subject') or request.POST.get('subject', '测试支付')

    # 3. 验证金额参数
    if not amount:
        return JsonResponse({"error": "缺少金额参数"}, status=400)

    try:
        # 确保金额是有效的数字且≥0.01
        amount_dec = decimal.Decimal(amount)
        if amount_dec < decimal.Decimal("0.01"):
            raise ValueError
    except (decimal.InvalidOperation, ValueError):
        return JsonResponse({"error": "金额必须为不小于0.01的数字"}, status=400)

    # 4. 初始化支付宝客户端（保持不变）
    try:
        with open(settings.ALIPAY_APP_PRIVATE_KEY_PATH) as f:
            private_key = f.read().strip()

        with open(settings.ALIPAY_PUBLIC_KEY_PATH) as f:
            public_key = f.read().strip()

        alipay = AliPay(
            appid=settings.ALIPAY_APPID,
            app_notify_url="http://example.com/notify",
            app_private_key_string=private_key,
            alipay_public_key_string=public_key,
            sign_type="RSA2",
            debug=True
        )

        # 5. 创建支付订单（使用动态金额）
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=f"pay_{int(time.time())}",
            total_amount=str(amount_dec),  # 动态传入的金额
            subject=subject,
            return_url="http://localhost:8080/"
        )

        pay_url = f"https://openapi-sandbox.dl.alipaydev.com/gateway.do?{order_string}"
        return JsonResponse({
            "pay_url": pay_url,
            "amount": str(amount_dec),
            "subject": subject
        })

    except Exception as e:
        return JsonResponse({"error": f"支付订单生成失败: {str(e)}"}, status=500)