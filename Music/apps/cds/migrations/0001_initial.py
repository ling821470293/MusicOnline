# Generated by Django 2.0 on 2019-04-19 10:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CDs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_id', models.CharField(max_length=50, verbose_name='专辑编号')),
                ('name', models.CharField(max_length=100, verbose_name='专辑名')),
                ('cds_front_image', models.ImageField(blank=True, null=True, upload_to='cds/images/', verbose_name='封面图')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='上传时间')),
            ],
            options={
                'verbose_name': '专辑',
                'verbose_name_plural': '专辑',
            },
        ),
    ]
