# Generated by Django 3.0.8 on 2020-08-15 12:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cmt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cmt',
            name='post_id',
        ),
        migrations.AddField(
            model_name='cmt',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cmt',
            name='user_name',
            field=models.CharField(default=datetime.datetime(2020, 8, 15, 12, 46, 58, 422075, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
