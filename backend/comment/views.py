from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Comment
from .serializers import CommentSerializer
from person.models import Person
from products.models import Product

# 添加评论
@api_view(["POST"])
def add_comment(request, product_id):
    """添加评论（用户登录即可）"""
    user_id = request.session.get("user_id")
    if not user_id:
        return Response({"error": "用户未登录"}, status=status.HTTP_401_UNAUTHORIZED)

    user = get_object_or_404(Person, id=user_id)
    product = get_object_or_404(Product, id=product_id)

    text = request.data.get("text", "").strip()
    image = request.FILES.get("image")  # 获取图片（如果有）

    if not text and not image:
        return Response({"error": "评论内容不能为空"}, status=status.HTTP_400_BAD_REQUEST)

    # 创建评论对象，文字和图片都可以为空
    comment = Comment.objects.create(user=user, product=product, text=text, image=image if image else None)
    serializer = CommentSerializer(comment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

# 删除评论
@api_view(["DELETE"])
def delete_comment(request, comment_id):
    """删除评论（仅评论发布者可以删除）"""
    user_id = request.session.get("user_id")
    if not user_id:
        return Response({"error": "用户未登录"}, status=status.HTTP_401_UNAUTHORIZED)

    comment = get_object_or_404(Comment, id=comment_id)

    if comment.user.id != user_id:
        return Response({"error": "无权限删除该评论"}, status=status.HTTP_403_FORBIDDEN)

    comment.delete()
    return Response({"message": "评论已删除"}, status=status.HTTP_200_OK)

# 获取商品评论
@api_view(["GET"])
def get_product_comments(request, product_id):
    """获取某个商品的所有评论"""
    product = get_object_or_404(Product, id=product_id)
    comments = Comment.objects.filter(product=product).order_by("-created_at")
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
from django.shortcuts import render

# Create your views here.
