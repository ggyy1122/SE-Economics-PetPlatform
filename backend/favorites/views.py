from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Favorite
from person.models import Person
from products.models import Product
from .serializers import FavoriteSerializer


@api_view(["POST"])
def AddFavorite(request):
    """添加收藏"""
    user_id = request.session.get("user_id")
    if not user_id:
        return Response({"error": "用户未登录"}, status=status.HTTP_401_UNAUTHORIZED)

    product_id = request.data.get("product_id")
    if not product_id:
        return Response({"error": "缺少商品 ID"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = Person.objects.get(id=user_id)
        product = Product.objects.get(id=product_id)

        # 检查是否已收藏
        if Favorite.objects.filter(user=user, product=product).exists():
            return Response({"message": "该商品已在收藏列表"}, status=status.HTTP_200_OK)

        favorite_data = {"user": user.id, "product": product.id}
        serializer = FavoriteSerializer(data=favorite_data)
        if serializer.is_valid():
            serializer.save(user=user)  # 由于 user 是 read_only_fields，所以手动赋值
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Person.DoesNotExist:
        return Response({"error": "用户不存在"}, status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return Response({"error": "商品不存在"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def RemoveFavorite(request):
    """取消收藏"""
    user_id = request.session.get("user_id")
    if not user_id:
        return Response({"error": "用户未登录"}, status=status.HTTP_401_UNAUTHORIZED)

    product_id = request.data.get("product_id")
    if not product_id:
        return Response({"error": "缺少商品 ID"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = Person.objects.get(id=user_id)
        product = Product.objects.get(id=product_id)

        favorite = Favorite.objects.filter(user=user, product=product)
        if favorite.exists():
            favorite.delete()
            return Response({"message": "取消收藏成功"}, status=status.HTTP_200_OK)
        return Response({"message": "该商品未收藏"}, status=status.HTTP_200_OK)

    except Person.DoesNotExist:
        return Response({"error": "用户不存在"}, status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return Response({"error": "商品不存在"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def checkFavoriteStatus(request):
    """检查用户是否收藏了某商品"""
    user_id = request.session.get("user_id")
    if not user_id:
        return Response({"error": "用户未登录"}, status=status.HTTP_401_UNAUTHORIZED)

    product_id = request.GET.get("product_id")
    if not product_id:
        return Response({"error": "缺少商品 ID"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = Person.objects.get(id=user_id)
        product = Product.objects.get(id=product_id)
        is_favorited = Favorite.objects.filter(user=user, product=product).exists()
        return Response({"is_favorited": is_favorited}, status=status.HTTP_200_OK)
    except (Person.DoesNotExist, Product.DoesNotExist):
        return Response({"error": "用户或商品不存在"}, status=status.HTTP_400_BAD_REQUEST)
