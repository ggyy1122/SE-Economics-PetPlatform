from rest_framework import serializers
from .models import Ad  # 导入广告模型



class AdSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = '__all__'  # 保留所有字段

    # 获取图片的完整 URL
    def get_image_url(self, obj):
        # 返回完整的图片 URL
        return f"http://127.0.0.1:8000{obj.image.url}"