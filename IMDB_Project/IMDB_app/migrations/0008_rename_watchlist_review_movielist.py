# Generated by Django 4.2.17 on 2024-12-20 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IMDB_app', '0007_rename_reviw_user_review_review_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='watchlist',
            new_name='movielist',
        ),
    ]
