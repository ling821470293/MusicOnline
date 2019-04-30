from django.shortcuts import render
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
# from rest_framework_extensions.cache.mixins import CacheResponseMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import CDsFilter
from .serializers import CDsSerializer
from .models import CDs
# from songs.models import Songs

# Create your views here.
class CDsViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    专辑详情
    """
    queryset = CDs.objects.all()
    serializer_class = CDsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = CDsFilter
