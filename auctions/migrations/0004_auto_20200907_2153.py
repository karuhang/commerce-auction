# Generated by Django 2.2.10 on 2020-09-07 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_wishlist'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wishlist',
            new_name='Watchlist',
        ),
    ]