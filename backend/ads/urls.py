# ads/urls.py
from django.urls import path
from .views import AdUploadAPIView
from . import views

urlpatterns = [
    path('upload/', AdUploadAPIView.as_view(), name='ad-upload'),
    path('ads/', views.homepage_ads, name='homepage_ads'),  # 通过 GET 请求获取 ads 广告
]