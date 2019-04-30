# -*- coding: utf-8 -*-

import django_filters
from django.db.models import Q

from .models import Songs


class SongsFilter(django_filters.rest_framework.FilterSet):
    """
    歌曲的过滤类
    """
    category = django_filters.NumberFilter(method='category_filter')


    def category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value))


    class Meta:
        model = Songs
        fields = ['name', 'is_hot']
