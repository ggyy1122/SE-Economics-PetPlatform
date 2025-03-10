##2025-3-7
##创建数据库的ad表


# Create your models here.
# ads/models.py
from django.db import models

from django.db import models
from django.utils import timezone

class Ad(models.Model):
    image = models.ImageField(upload_to='ads/', max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)  # 手动提供默认值

