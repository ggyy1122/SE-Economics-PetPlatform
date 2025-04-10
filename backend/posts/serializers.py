from rest_framework import serializers
from .models import Post, Content, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['text', 'image', 'video']

class PostSerializer(serializers.ModelSerializer):
    content = ContentSerializer()
    tags = TagSerializer(many=True, required=False)
    user = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'user', 'created_at', 'updated_at', 'tags', 'content']

    def create(self, validated_data):
        content_data = validated_data.pop('content')
        tags_data = validated_data.pop('tags', [])

        # 获取当前用户
        request = self.context.get('request')
        user = getattr(request.user, 'person', None) if request else None

        # 创建帖子
        post = Post.objects.create(user=user, **validated_data)

        # 创建内容
        Content.objects.create(post=post, **content_data)

        # 处理标签（自动创建不存在的标签）
        for tag_dict in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_dict['name'])
            post.tags.add(tag)

        return post

    def update(self, instance, validated_data):
        content_data = validated_data.pop('content', None)
        tags_data = validated_data.pop('tags', [])

        instance.title = validated_data.get('title', instance.title)
        instance.save()

        # 更新内容
        if content_data:
            content = instance.content
            content.text = content_data.get('text', content.text)
            content.image = content_data.get('image', content.image)
            content.video = content_data.get('video', content.video)
            content.save()

        # 更新标签
        instance.tags.clear()
        for tag_dict in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_dict['name'])
            instance.tags.add(tag)

        return instance
