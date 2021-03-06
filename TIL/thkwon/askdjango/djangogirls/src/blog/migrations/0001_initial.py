# Generated by Django 2.1.7 on 2019-03-29 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('text', models.TextField(verbose_name='내용')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='생성 시간')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='발행 시간')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='authors')),
            ],
        ),
    ]
