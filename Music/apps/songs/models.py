from DjangoUeditor.models import UEditorField
from cds.models import CDs
from singers.models import Singers
from datetime import datetime
from django.db import models

class SongsCategory(models.Model):
    """
    歌曲类别
    """
    # CATEGORY_TYPE = (
    #     (1, "一级类目"),
    #     (2, "二级类目"),
    #     (3, "三级类目"),
    # )

    name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    code = models.CharField(default="", max_length=30, verbose_name="类别编号", help_text="类别编号")
    # desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    # category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类别级目", help_text="类别级目")
    # parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
    #                                     related_name="sub_cat")
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    # add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "歌曲类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Songs(models.Model):
    """
    歌曲
    """
    category = models.ForeignKey(SongsCategory, on_delete=models.CASCADE, verbose_name="歌曲类目")
    cd_id = models.ForeignKey(CDs, related_name="cdname", on_delete=models.CASCADE, null=True, blank=True,  verbose_name="所属专辑")
    song_id = models.CharField(max_length=50, verbose_name="歌曲编号")
    name = models.CharField(max_length=100, verbose_name="歌曲名")
    singer_id = models.ForeignKey(Singers, related_name="singername",on_delete=models.CASCADE, verbose_name="歌手")
    publish_date = models.DateTimeField(null=True, blank=True, verbose_name="发行时间")
    file = models.FileField(upload_to="songs/files/", verbose_name="上传的歌曲", help_text="上传的歌曲")
    click_num = models.IntegerField(null=True, blank=True, default=0, verbose_name="点击数")
    download_num = models.IntegerField(null=True, blank=True, default=0, verbose_name="歌曲下载量")
    fav_num = models.IntegerField(null=True, blank=True, default=0, verbose_name="收藏数")
    songs_brief = models.TextField(null=True, blank=True, max_length=500, verbose_name="歌曲简短描述")
    geci = models.TextField(null=True, blank=True, verbose_name="歌词")
    is_hot = models.BooleanField(default=False, verbose_name="热门推荐")
    songs_front_image = models.ImageField(upload_to="songs/images/", null=True, blank=True, verbose_name="封面图")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="上传时间")

    class Meta:
        verbose_name = '歌曲'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class IndexAd(models.Model):
    category = models.ForeignKey(SongsCategory, related_name='category',verbose_name="歌曲类目", on_delete=models.CASCADE)
    songs =models.ForeignKey(Songs, related_name='songs', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '首页歌曲类别广告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.songs.name

class HotSearchWords(models.Model):
    """
    热搜词
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="热搜词")
    index = models.IntegerField(default=0, verbose_name="排序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '热搜词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords