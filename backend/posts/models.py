# 2025-4-7 初尝试构建社区帖子
from django.db import models
from person.models import Person  # 引入你已有的用户模型 Person

# posts/models.py

class Post(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return f"{self.title} by {self.user.name}"

class Content(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)  # 每个帖子对应一个内容
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='posts/images/', blank=True, null=True)
    video = models.FileField(upload_to='posts/videos/', blank=True, null=True)

    def __str__(self):
        return f"Content of {self.post.title}"

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
