#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import Singers

class SingersAdmin(object):
    list_display = ["name", "singer_id", "birthday", "gender", "desc", "country", "add_time"]
    search_fields = ['name', ]
    list_filter = ["name", "singer_id", "birthday", "gender", "desc", "country", "add_time"]


xadmin.site.register(Singers, SingersAdmin)
