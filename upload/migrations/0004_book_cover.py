# Generated by Django 3.0.4 on 2020-03-21 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_remove_book_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='books/cover/'),
        ),
    ]