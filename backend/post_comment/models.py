# 2025-4-13 帖子评论区制作
from django.db import models
from person.models import Person
from posts.models import Post  # 假设帖子模型在 posts 应用中

class PostComment(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='post_comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_comments/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.name} on Post: {self.post.title}"

    class Meta:
        ordering = ['-created_at']
