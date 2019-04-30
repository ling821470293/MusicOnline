# -*- coding: utf-8 -*-

from rest_framework import serializers
from songs.models import Songs
from cds.models import CDs

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = "__all__"

class CDsSerializer(serializers.ModelSerializer):
    cdname = SongsSerializer(many=True)
    class Meta:
        model = CDs
        fields = "__all__"

