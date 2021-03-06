# Generated by Django 2.2 on 2019-04-10 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190410_1740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('p', 'Published'), ('d', 'Draft'), ('w', 'Withdrawn')], max_length=1),
        ),
        migrations.AddField(
            model_name='post',
            name='tag_set',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
