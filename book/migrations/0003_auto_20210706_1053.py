# Generated by Django 3.2.5 on 2021-07-06 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_book_author_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='book.Author'),
        ),
        migrations.DeleteModel(
            name='Book_Author',
        ),
    ]
