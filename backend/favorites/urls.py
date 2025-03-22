from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddFavorite, name='add_favorite'),  # 添加收藏
    path('remove/', views.RemoveFavorite, name='remove_favorite'),  # 取消收藏
    path('check_status/', views.checkFavoriteStatus, name='check_favorite'),  # 取消收藏
]
