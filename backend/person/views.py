from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Person
from django.views.decorators.csrf import csrf_exempt
from .serializers import RegisterSerializer, LoginSerializer, PersonSerializer
import json

@api_view(["POST"])
def register_view(request):
    """用户注册"""
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        request.session["user_id"] = user.id
        request.session["name"] = user.name
        return Response({"message": "注册成功", "name": user.name})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt  # 豁免CSRF验证仅用于登录接口
@api_view(["POST"])
def login_view(request):
    """用户登录"""
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data["name"]
        password = serializer.validated_data["password"]

        try:
            user = Person.objects.get(name=name)
            if check_password(password, user.password):  # 进行密码校验
                request.session["user_id"] = user.id
                request.session["name"] = user.name

                return Response({"message": "登录成功", "name": user.name})
            else:
                return Response({"error": "密码错误"}, status=status.HTTP_400_BAD_REQUEST)
        except Person.DoesNotExist:
            return Response({"error": "用户名不存在"}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_user_info(request):
    """获取当前登录用户信息"""
    user_id = request.session.get("user_id")
    if user_id:
        user = Person.objects.get(id=user_id)
        serializer = PersonSerializer(user)
        return Response(serializer.data)
    return Response({"error": "未登录"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
def logout_view(request):
    """用户退出"""
    request.session.flush()  # 清空 session
    return Response({"message": "退出成功"})

@api_view(["GET"])
def check_login_status(request):
    """检测当前用户是否已登录"""
    user_id = request.session.get("user_id")
    if user_id:
        user = Person.objects.get(id=user_id)
        return Response({"message": f"用户已登录"})
    return Response({"message": "用户未登录"}, status=status.HTTP_401_UNAUTHORIZED)
