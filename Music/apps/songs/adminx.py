#!/usr/bin/env python
# encoding: utf-8

import xadmin
from .models import SongsCategory, Songs, HotSearchWords

class SongsAdmin(object):
    list_display = ["category", "cd_id", "song_id", "name", "singer_id", "publish_date",
                    "click_num", "download_num", "fav_num", "songs_brief", "add_time"]
    search_fields = ['name', ]
    list_filter = ["name", "click_num", "category", "fav_num", "cd_id", "song_id",
                   "singer_id", "add_time"]


class SongsCategoryAdmin(object):
    list_display = ["name",]
    list_filter = ["name",]
    search_fields = ['name', ]


class HotSearchAdmin(object):
    list_display = ["keywords", "index", "add_time"]


xadmin.site.register(Songs, SongsAdmin)
xadmin.site.register(SongsCategory, SongsCategoryAdmin)
xadmin.site.register(HotSearchWords, HotSearchAdmin)

