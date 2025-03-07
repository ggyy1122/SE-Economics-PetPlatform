from django.urls import path
from . import views
####  http://127.0.0.1:8000/api/testapi/products/
urlpatterns = [
    path('products/', views.get_products, name='get_products'),
]
