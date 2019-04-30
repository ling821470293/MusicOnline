# Generated by Django 2.0 on 2019-04-29 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operations', '0003_userleavingmessage_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userleavingmessage',
            name='message_type',
            field=models.IntegerField(choices=[(1, '留言'), (2, '建议'), (3, '上传')], default=1, help_text='留言类型: 1(留言),2(建议),3(上传)', verbose_name='留言类型'),
        ),
    ]
