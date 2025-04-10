from django.urls import path
from .views import add_post, list_tags, PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')

urlpatterns = [
    path('create/', add_post, name='add_post'),
    path('tags/', list_tags, name='list_tags'),
]

urlpatterns += router.urls
