# Generated by Django 2.0 on 2019-04-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='psd',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='user_id',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='称呼'),
        ),
    ]