# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.db.models import Q
from songs.models import Songs, SongsCategory, HotSearchWords
from songs.models import IndexAd
from cds.models import CDs
from singers.models import Singers

class SingersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singers
        fields = "__all__"

class CDsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CDs
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SongsCategory
        fields = "__all__"

class SongsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    cd_id = CDsSerializer()
    singer_id = SingersSerializer()
    class Meta:
        model = Songs
        fields = "__all__"

class HotWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotSearchWords
        fields = "__all__"

class IndexCategorySerializer(serializers.ModelSerializer):
    songs = serializers.SerializerMethodField()
    ad_songs = serializers.SerializerMethodField()

    def get_ad_songs(self, obj):
        songs_json = {}
        ad_songs = IndexAd.objects.filter(category_id=obj.id, )
        if ad_songs:
            song_ins = ad_songs[0].songs
            songs_json = SongsSerializer(song_ins, many=False, context={'request': self.context['request']}).data
        return songs_json



    def get_songs(self, obj):
        all_songs = Songs.objects.all()
        songs_serializer = SongsSerializer(all_songs, many=True, context={'request': self.context['request']})
        return songs_serializer.data

    class Meta:
        model = SongsCategory
        fields = "__all__"
