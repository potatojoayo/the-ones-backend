# Generated by Django 3.2.5 on 2021-07-06 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20210706_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='release_date',
        ),
        migrations.AddField(
            model_name='movie',
            name='title_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(default=0),
        ),
    ]
