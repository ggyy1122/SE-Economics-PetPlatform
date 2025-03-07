from django.urls import path
from . import views  # 引入视图文件

urlpatterns = [
    path('your-endpoint/', views.your_view),  # 你需要定义的 URL 路径
]
