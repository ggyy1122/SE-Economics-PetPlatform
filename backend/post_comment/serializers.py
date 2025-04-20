from rest_framework import serializers
from .models import PostComment

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = ['id', 'user', 'post', 'text', 'image', 'created_at']
