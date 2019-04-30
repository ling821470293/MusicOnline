from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from songs.models import Songs

# Create your models here.
User = get_user_model()


class UserFav(models.Model):
    """
    用户收藏
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    songs = models.ForeignKey(Songs, on_delete=models.CASCADE, verbose_name="歌曲", help_text="歌曲id")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "songs")

    def __str__(self):
        return self.user.name


class UserLeavingMessage(models.Model):
    """
    用户留言
    """
    MESSAGE_CHOICES = (
        (1, "留言"),
        (2, "建议"),
        (3, "上传")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="留言类型",
                                       help_text=u"留言类型: 1(留言),2(建议),3(上传)")
    subject = models.CharField(max_length=100, default="", verbose_name="主题")
    message = models.TextField(default="", verbose_name="留言内容", help_text="留言内容")
    file = models.FileField(upload_to="message/files/", default='', verbose_name="上传的文件", help_text="上传的文件")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject