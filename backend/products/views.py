from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import Product
from .serializers import ProductSerializer


class ProductPagination(PageNumberPagination):
    page_size = 100  # 默认每页10个
    page_size_query_param = 'page_size'
    max_page_size = 100  # 最大100个
    max_limit = 50  # 新增：limit参数的最大值

    def paginate_queryset(self, queryset, request, view=None):
        # 获取limit参数
        limit = request.query_params.get('limit')

        if limit is not None:
            try:
                limit = int(limit)
                # 验证limit值是否在合理范围内
                if limit <= 0:
                    raise ValidationError("limit参数必须大于0")
                if limit > self.max_limit:
                    raise ValidationError(f"limit参数最大不能超过{self.max_limit}")

                # 如果limit有效，则直接截取结果而不分页
                return list(queryset[:limit])
            except ValueError:
                raise ValidationError("limit参数必须是整数")

        # 如果没有limit参数，则使用正常分页
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        # 检查是否使用了limit参数（通过检查self.page是否存在）
        if not hasattr(self, 'page'):
            return Response({
                'results': data,
                'limit': len(data)  # 返回实际获取的数量
            })

        # 正常的分页响应
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'results': data
        })


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'price': ['exact', 'lt', 'lte', 'gt', 'gte'],
        'stock': ['exact', 'gte'],
        'animals__name': ['exact', 'icontains'],
        'categories__name': ['exact', 'icontains'],
    }
    ordering_fields = ['price', 'stock']
    ordering = ['id']

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params

        name = params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset