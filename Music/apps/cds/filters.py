# -*- coding: utf-8 -*-

import django_filters
from django.db.models import Q

from .models import CDs


class CDsFilter(django_filters.rest_framework.FilterSet):
    """
    专辑的过滤类
    """
    class Meta:
        model = CDs
        fields = ['name', 'is_recommend']
