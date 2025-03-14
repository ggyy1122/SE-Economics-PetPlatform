from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Person(models.Model):
    name = models.CharField(max_length=150, unique=True)  # 用户名，唯一
    password = models.CharField(max_length=128)  # 存储加密后的密码
    email = models.EmailField(unique=True, null=True, blank=True)  # 邮箱（可选）
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)  # 手机号（可选）
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)  # 头像（可选）
    created_at = models.DateTimeField(auto_now_add=True)  # 注册时间
    updated_at = models.DateTimeField(auto_now=True)  # 最后更新时间

    def set_password(self, raw_password):
        """加密存储密码"""
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        """验证密码"""
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.name
