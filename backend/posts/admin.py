# posts/admin.py
from django.contrib import admin
from .models import Post, Content, Tag

admin.site.register(Post)
admin.site.register(Content)
admin.site.register(Tag)
