from django.urls import path
from .views import get_user_orders,create_order

from . import views

urlpatterns = [
    path('notify/', views.alipay_notify, name='alipay_notify'),
    path('orders/user/', get_user_orders, name='user_orders'),
    path('create_order/', create_order),
]
