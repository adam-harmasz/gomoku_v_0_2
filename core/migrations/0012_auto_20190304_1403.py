# Generated by Django 2.1.5 on 2019-03-04 14:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_userprofile_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 4, 14, 3, 24, 588000, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='created'),
        ),
    ]