# Generated by Django 2.1.5 on 2019-01-31 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gomokurecordfile',
            name='file_path',
        ),
    ]
