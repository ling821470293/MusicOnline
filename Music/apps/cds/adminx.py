#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import CDs

class CDsAdmin(object):
    list_display = ["cd_id", "name", "add_time"]
    search_fields = ['name', ]
    list_filter = ["cd_id", "name", "add_time"]


xadmin.site.register(CDs, CDsAdmin)
