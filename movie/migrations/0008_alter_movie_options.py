# Generated by Django 3.2.5 on 2021-07-07 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20210707_1323'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['popularity']},
        ),
    ]
