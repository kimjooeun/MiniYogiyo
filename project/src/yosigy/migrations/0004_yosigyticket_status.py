# Generated by Django 2.1 on 2019-06-13 05:03

from django.db import migrations, models
import yosigy.models


class Migration(migrations.Migration):

    dependencies = [
        ('yosigy', '0003_yosigyticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='yosigyticket',
            name='status',
            field=models.IntegerField(choices=[(1, '미발행'), (2, '발행'), (3, '사용'), (4, '취소')], default=yosigy.models.YosigyTiketStatus(1), verbose_name='상태'),
        ),
    ]
