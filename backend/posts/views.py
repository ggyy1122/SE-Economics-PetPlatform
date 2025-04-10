from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.db import transaction

from person.models import Person
from .models import Post, Tag, Content
from .serializers import PostSerializer, TagSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


@api_view(["POST"])
def add_post(request):
    """添加帖子（用户登录即可）"""
    # 从 session 中获取 user_id，确保用户已经登录
    user_id = request.session.get("user_id")
    if not user_id:
        return Response({"error": "用户未登录"}, status=status.HTTP_401_UNAUTHORIZED)

    # 获取当前用户对象
    user = get_object_or_404(Person, id=user_id)

    # 获取前端提交的数据
    title = request.data.get("title", "").strip()
    content_text = request.data.get("text", "").strip()
    image = request.FILES.get("image")  # 获取图片
    video = request.FILES.get("video")  # 获取视频
    tags = request.data.get("tags", [])  # 标签列表：["tag1", "tag2"]

    # 校验数据，标题不能为空，内容也不能都为空
    if not title or (not content_text and not image and not video):
        return Response({"error": "标题和内容不能全部为空"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        with transaction.atomic():
            # 创建帖子
            post = Post.objects.create(user=user, title=title)

            # 创建内容
            Content.objects.create(post=post, text=content_text, image=image, video=video)

            for tag_id in tags:
                try:
                    tag = Tag.objects.get(id=int(tag_id))
                    post.tags.add(tag)
                except Tag.DoesNotExist:
                    continue

        # 返回成功响应，帖子数据通过序列化返回
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
def list_tags(request):
    """获取所有标签"""
    tags = Tag.objects.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
