from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_comment, name='add_comment'),
    path('delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('product/<int:product_id>/', views.get_product_comments, name='get_product_comments'),
]
