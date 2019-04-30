from datetime import datetime
from django.db import models
# from songs.models import Songs

class CDs(models.Model):
    """
    专辑
    """
    cd_id = models.CharField(max_length=50, verbose_name="专辑编号", help_text="专辑编号")
    name = models.CharField(max_length=100, verbose_name="专辑名", help_text="专辑名")
    cds_front_image = models.ImageField(upload_to="cds/images/", null=True, blank=True, verbose_name="封面图", help_text="专辑封面图")
    is_recommend = models.BooleanField(default=False, verbose_name="热门推荐", help_text="是否为热门推荐")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="上传时间", help_text="上传时间")

    class Meta:
        verbose_name = '专辑'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
