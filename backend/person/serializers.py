from rest_framework import serializers
from .models import Person
from django.contrib.auth.hashers import make_password

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            "id", "name", "email", "phone", "avatar",
            "gender", "birthday", "address",
            "created_at", "updated_at"
        ]

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["name", "password"]
        extra_kwargs = {
            "password": {"write_only": True},  # 确保密码不会被序列化返回
        }

    def create(self, validated_data):
        """重写 create 方法，确保密码加密存储"""
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)

class LoginSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)

class PersonUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["email", "phone", "avatar", "gender", "birthday", "address"]
        extra_kwargs = {
            "email": {"required": False, "allow_blank": True},
            "phone": {"required": False, "allow_blank": True},
            "avatar": {"required": False},
            "gender": {"required": False},
            "birthday": {"required": False},
            "address": {"required": False, "allow_blank": True},
        }

