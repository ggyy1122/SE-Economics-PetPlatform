"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static
from ads.views import homepage_ads
from ads import views  # 引入 ads 应用中的视图

# 创建路由
router = routers.DefaultRouter()
router.register(r'ads', views.AdViewSet)  # 为 ads API 注册视图集

urlpatterns = [
    path('admin/', admin.site.urls),  # Django 管理后台
    path('api/testapi/', include('testapi.urls')),  # 引入 testapi 的路由
    path('api/ads/', include(router.urls)),      #引入 ads 的路由
    path('api/ads/homepage/', homepage_ads, name='homepage-ads'),  # 定义获取首页广告的路由
    path('api/', include('products.urls')),  # 包含 products 应用的路由
    path('api/person/', include('person.urls')),
    path('api/favorites/', include('favorites.urls')),  # 包含 favorites 应用的路由
    path('api/cart/', include('cart.urls')),  # 引入 cart 应用的路由
    path('api/comments/', include('comment.urls')),  # 添加评论模块的路由
]

# 关键部分：让 Django 处理 media 文件
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)