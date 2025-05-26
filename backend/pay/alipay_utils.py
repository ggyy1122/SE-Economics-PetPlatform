from alipay import AliPay
from django.conf import settings
import os


def get_alipay_client():
    # 添加密钥文件存在性检查
    if not os.path.exists(settings.ALIPAY_APP_PRIVATE_KEY_PATH):
        raise FileNotFoundError(f"私钥文件不存在: {settings.ALIPAY_APP_PRIVATE_KEY_PATH}")
    if not os.path.exists(settings.ALIPAY_PUBLIC_KEY_PATH):
        raise FileNotFoundError(f"公钥文件不存在: {settings.ALIPAY_PUBLIC_KEY_PATH}")

    with open(settings.ALIPAY_APP_PRIVATE_KEY_PATH, 'r') as f:
        private_key = f.read()

    with open(settings.ALIPAY_PUBLIC_KEY_PATH, 'r') as f:
        public_key = f.read()

    return AliPay(
        appid=settings.ALIPAY_APPID,
        app_notify_url=getattr(settings, 'ALIPAY_NOTIFY_URL', 'http://default.com/notify'),
        app_private_key_string=private_key,
        alipay_public_key_string=public_key,
        sign_type="RSA2",
        debug=True  # 沙箱环境必须为True
    )