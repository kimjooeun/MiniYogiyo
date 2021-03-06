# Generated by Django 2.1 on 2019-05-20 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='estimated_delivery_time',
            field=models.TimeField(verbose_name='배달예상시간'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='operation_end_hour',
            field=models.TimeField(verbose_name='영업종료시간'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='operation_start_hour',
            field=models.TimeField(verbose_name='영업시작시간'),
        ),
    ]
