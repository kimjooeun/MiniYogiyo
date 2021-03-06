# Generated by Django 2.1 on 2019-06-13 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20190612_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='menutimeline',
            name='post_menu_is_set_menu',
            field=models.BooleanField(blank=True, default=False, verbose_name='변경 후 세트 메뉴 여부'),
        ),
        migrations.AddField(
            model_name='menutimeline',
            name='post_menu_is_yosigy',
            field=models.BooleanField(blank=True, default=False, verbose_name='변경 후 요식이 메뉴 여부'),
        ),
        migrations.AddField(
            model_name='menutimeline',
            name='prior_menu_is_set_menu',
            field=models.BooleanField(blank=True, default=False, verbose_name='변경 전 세트 메뉴 여부'),
        ),
        migrations.AddField(
            model_name='menutimeline',
            name='prior_menu_is_yosigy',
            field=models.BooleanField(blank=True, default=False, verbose_name='변경 전 요식이 메뉴 여부'),
        ),
    ]
