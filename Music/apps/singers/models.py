from datetime import datetime
from django.db import models

class Singers(models.Model):
    """
    歌手
    """
    singer_id = models.CharField(max_length=50, default="", verbose_name="歌手编号")
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female",
                              verbose_name="性别")
    desc = models.TextField(null=True, blank=True, verbose_name='歌手介绍')
    country = models.CharField(max_length=50, null=True, blank=True, verbose_name='歌手国籍')
    singer_images = models.ImageField(upload_to="singers/images/", null=True, blank=True, verbose_name="歌手照片")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '歌手'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
