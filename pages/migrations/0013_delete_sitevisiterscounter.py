# Generated by Django 4.1 on 2022-08-29 03:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_remove_gamevote_game_type_remove_gamevote_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SiteVisitersCounter',
        ),
    ]
