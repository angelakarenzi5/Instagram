# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-27 10:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pictures', '0006_auto_20190326_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='image',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='image',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='comments',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pictures.Image'),
        ),
        migrations.AddField(
            model_name='comments',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pictures.Profile'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
