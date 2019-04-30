from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .serializers import SongsSerializer, CategorySerializer, IndexCategorySerializer, HotWordsSerializer
from .models import Songs, SongsCategory, HotSearchWords
from .filters import SongsFilter
# Create your views here.


class SongsPagination(PageNumberPagination):
    """
    歌曲分页设置
    """
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class SongsListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    歌曲列表页
    """
    # throttle_classes = (UserRateThrottle, )
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    pagination_class = SongsPagination
    # # authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = SongsFilter
    search_fields = ('name', 'songs_brief', 'geci')
    ordering_fields = ('click_num', 'download_num', 'fav_num')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        歌曲分类列表数据
    retrieve:
        获取歌曲分类详情
    """
    queryset = SongsCategory.objects.all()
    serializer_class = CategorySerializer

class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页歌曲分类数据
    """
    queryset = SongsCategory.objects.filter(is_tab=True)
    serializer_class = IndexCategorySerializer

class HotSearchsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取热搜词列表
    """
    queryset = HotSearchWords.objects.all().order_by("-index")
    serializer_class = HotWordsSerializer