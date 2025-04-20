from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import PostComment
from .serializers import PostCommentSerializer
from person.models import Person
from posts.models import Post

@api_view(["POST"])
def add_post_comment(request, post_id):
    user_id = request.session.get("user_id")
    if not user_id:
        return Response({"error": "用户未登录"}, status=status.HTTP_401_UNAUTHORIZED)

    user = get_object_or_404(Person, id=user_id)
    post = get_object_or_404(Post, id=post_id)

    text = request.data.get("text", "").strip()
    image = request.FILES.get("image")

    if not text and not image:
        return Response({"error": "评论内容不能为空"}, status=status.HTTP_400_BAD_REQUEST)

    comment = PostComment.objects.create(user=user, post=post, text=text, image=image if image else None)
    serializer = PostCommentSerializer(comment)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["DELETE"])
def delete_post_comment(request, comment_id):
    user_id = request.session.get("user_id")
    if not user_id:
        return Response({"error": "用户未登录"}, status=status.HTTP_401_UNAUTHORIZED)

    comment = get_object_or_404(PostComment, id=comment_id)

    if comment.user.id != user_id:
        return Response({"error": "无权限删除该评论"}, status=status.HTTP_403_FORBIDDEN)

    comment.delete()
    return Response({"message": "评论已删除"}, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_post_comments(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = PostComment.objects.filter(post=post).order_by("-created_at")
    serializer = PostCommentSerializer(comments, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
