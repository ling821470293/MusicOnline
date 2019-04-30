# -*- coding: utf-8 -*-

from rest_framework import serializers
from songs.models import Songs, SongsCategory, HotSearchWords
from cds.models import CDs
from singers.models import Singers

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = "__all__"

class SingersSerializer(serializers.ModelSerializer):
    singername = SongsSerializer(many=True)
    class Meta:
        model = Singers
        fields = "__all__"


