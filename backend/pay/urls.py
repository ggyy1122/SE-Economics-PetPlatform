from django.urls import path
from .views import create_payment
# from .views import create_payment  # 明确导入视图函数

urlpatterns = [
    #path('create/', create_payment, name='alipay_create_payment'),  # 去掉重复路径
    path('create_payment/', create_payment),  # 新增临时路由
]