from django.shortcuts import render
##2025-3-7
##创建ad api的视图
# Create your views here.
# ads/views.py
from rest_framework import viewsets
from .models import Ad  # 导入广告模型
from .serializers import AdSerializer  # 导入广告序列化器
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer

# 2025-03-09: 用于操作数据库的视图 广告API视图
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all().order_by('-created_at')  # 获取所有广告，并按时间降序排列
    serializer_class = AdSerializer  # 使用 AdSerializer 来序列化广告数据

# 2025-03-09: 获取首页广告的 API 视图
# 它从数据库中获取广告数据，并 以 JSON 格式返回
# 创建一个返回homepage广告的API视图
@api_view(['GET'])
@renderer_classes([JSONRenderer])  # 指定只用 JSON 渲染
def homepage_ads(request):
    # 获取符合条件的广告数据
    ads = Ad.objects.filter(location='homepage').values('id', 'image', 'created_at')
    # 构造返回数据，包括图片的完整 URL
    ads_data = []
    for ad in ads:
        ads_data.append({
            'id': ad['id'],
            'image_url': ad['image'],  # 这里假设 `image` 字段本身就是图片的路径
            'created_at': ad['created_at'].strftime('%Y-%m-%d %H:%M:%S')  # 格式化时间戳
        })

    return Response(ads_data)
