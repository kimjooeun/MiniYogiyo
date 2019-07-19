# Generated by Django 2.2 on 2019-04-09 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190409_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('w', 'Withdrawn'), ('d', 'Draft'), ('p', 'Published')], default='d', max_length=1),
            preserve_default=False,
        ),
    ]