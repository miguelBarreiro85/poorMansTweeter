# Generated by Django 2.1.1 on 2018-09-30 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='tweet_txt',
            new_name='tweet_text',
        ),
    ]
