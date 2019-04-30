from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
# from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .serializers import SingersSerializer
from .models import Singers

# Create your views here.
class SingerViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    歌手详情
    """
    queryset = Singers.objects.all()
    serializer_class = SingersSerializer