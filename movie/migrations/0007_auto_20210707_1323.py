# Generated by Django 3.2.5 on 2021-07-07 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20210707_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='image_path',
            new_name='poster_path',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
    ]
