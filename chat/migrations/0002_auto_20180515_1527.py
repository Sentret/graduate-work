# Generated by Django 2.0.4 on 2018-05-15 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='addresser',
        ),
        migrations.RemoveField(
            model_name='message',
            name='recipient',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
