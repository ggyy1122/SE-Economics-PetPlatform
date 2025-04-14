from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:post_id>/', views.add_post_comment, name='add_post_comment'),
    path('delete/<int:comment_id>/', views.delete_post_comment, name='delete_post_comment'),
    path('post/<int:post_id>/', views.get_post_comments, name='get_post_comments'),
]
