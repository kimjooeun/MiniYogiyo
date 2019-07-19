# Generated by Django 2.1 on 2019-05-24 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20190520_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='is_recommended',
            field=models.BooleanField(default=False, verbose_name='사장님 추천 메뉴인가?'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='score',
            field=models.FloatField(default=0.0, verbose_name='점수'),
        ),
    ]