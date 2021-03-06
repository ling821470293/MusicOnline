# Generated by Django 2.0 on 2019-04-19 10:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cds', '0001_initial'),
        ('singers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotSearchWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(default='', max_length=20, verbose_name='热搜词')),
                ('index', models.IntegerField(default=0, verbose_name='排序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '热搜词',
                'verbose_name_plural': '热搜词',
            },
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_id', models.CharField(max_length=50, verbose_name='歌曲编号')),
                ('name', models.CharField(max_length=100, verbose_name='歌曲名')),
                ('publish_date', models.DateTimeField(blank=True, null=True, verbose_name='发行时间')),
                ('file', models.FileField(help_text='上传的歌曲', upload_to='songs/files/', verbose_name='上传的歌曲')),
                ('click_num', models.IntegerField(blank=True, default=0, null=True, verbose_name='点击数')),
                ('download_num', models.IntegerField(blank=True, default=0, null=True, verbose_name='歌曲下载量')),
                ('fav_num', models.IntegerField(blank=True, default=0, null=True, verbose_name='收藏数')),
                ('songs_brief', models.TextField(blank=True, max_length=500, null=True, verbose_name='歌曲简短描述')),
                ('geci', models.TextField(blank=True, null=True, verbose_name='歌词')),
                ('songs_front_image', models.ImageField(blank=True, null=True, upload_to='songs/images/', verbose_name='封面图')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='上传时间')),
            ],
            options={
                'verbose_name': '歌曲',
                'verbose_name_plural': '歌曲',
            },
        ),
        migrations.CreateModel(
            name='SongsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='类别名', max_length=30, verbose_name='类别名')),
                ('code', models.CharField(default='', help_text='类别编号', max_length=30, verbose_name='类别编号')),
                ('is_tab', models.BooleanField(default=False, help_text='是否导航', verbose_name='是否导航')),
            ],
            options={
                'verbose_name': '歌曲类别',
                'verbose_name_plural': '歌曲类别',
            },
        ),
        migrations.AddField(
            model_name='songs',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='songs.SongsCategory', verbose_name='歌曲类目'),
        ),
        migrations.AddField(
            model_name='songs',
            name='cd_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cds.CDs', verbose_name='所属专辑'),
        ),
        migrations.AddField(
            model_name='songs',
            name='singer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singers.Singers', verbose_name='歌手'),
        ),
    ]
