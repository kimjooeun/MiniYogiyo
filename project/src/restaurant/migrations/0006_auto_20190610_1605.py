# Generated by Django 2.1 on 2019-06-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_restauranttimeline_is_group_purchase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restauranttimeline',
            name='is_group_purchase',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='is_group_purchase',
            field=models.BooleanField(default=False, verbose_name='공구 허용 여부'),
        ),
    ]
