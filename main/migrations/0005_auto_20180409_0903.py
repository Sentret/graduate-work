# Generated by Django 2.0.3 on 2018-04-09 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_comment_parrent_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='parrent_comment',
            new_name='parrent',
        ),
    ]
