# Generated by Django 3.2.5 on 2021-07-07 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20210706_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image_path',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
