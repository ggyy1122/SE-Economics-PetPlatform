from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.get_user_cart, name='get_user_cart'),
    path('all/', views.get_all_carts, name='get_all_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update/<int:product_id>/', views.update_cart_item, name='update_cart_item'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]
