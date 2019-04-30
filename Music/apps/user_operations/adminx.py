#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import UserFav, UserLeavingMessage


class UserFavAdmin(object):
    list_display = ['user', 'songs', "add_time"]


class UserLeavingMessageAdmin(object):
    list_display = ['user', 'message_type', "message", "add_time"]


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)